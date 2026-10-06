import argparse
import json
import logging
import os
import platform
import shutil
import socket
import subprocess
import sys
import time
import smtplib

from datetime import datetime
from email.message import EmailMessage

# ============================================================
# CONFIGURATION
# ============================================================

CPU_WARNING = 70
CPU_CRITICAL = 90

MEMORY_WARNING = 70
MEMORY_CRITICAL = 90

SWAP_WARNING = 50
SWAP_CRITICAL = 80

DISK_WARNING = 70
DISK_CRITICAL = 90

INODE_WARNING = 70
INODE_CRITICAL = 90

TEMP_WARNING = 70
TEMP_CRITICAL = 90

DEFAULT_LOG_FILE = "/var/log/server_health_check.log"
DEFAULT_JSON_FILE = "/var/log/server_health_check.json"

# ============================================================
# ANSI COLORS
# ============================================================

RESET = "\033[0m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"


# ============================================================
# STATUS VALUES
# ============================================================

OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# ============================================================
# GLOBAL STATUS
# ============================================================

overall_status = OK


# ============================================================
# LOGGING
# ============================================================

logger = logging.getLogger("server_health_check")

def setup_logging(log_file):
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    # File handler
    try:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except PermissionError:
        print(
            f"{YELLOW} WARNING: Cannot write log file "
            f"{log_file}. Running without file logging.{RESET}"
        )

# ============================================================
# STATUS FUNCTIONS
# ============================================================

def status_text(status):
    if status == OK:
        return f"{GREEN}OK{RESET}"
    if status == WARNING:
        return f"{YELLOW}WARNING{RESET}"
    if status == CRITICAL:
        return f"{RED}CRITICAL{RESET}"
    return f"{RED}UNKNOWN{RESET}"

def update_overall_status(status):
    global overall_status
    if status == CRITICAL:
        overall_status = CRITICAL
    elif status == WARNING and overall_status != CRITICAL:
        overall_status = WARNING
    elif status == UNKNOWN and overall_status == OK:
        overall_status = UNKNOWN

def evaluate(value, warning, critical):
    if value >= critical:
        return CRITICAL
    if value >= warning:
        return WARNING
    return OK

# ============================================================
# DISPLAY
# ============================================================

def print_header(title):
    print()
    print(
        f"{BLUE}{'=' * 75}{RESET}"
    )
    print(
        f"{CYAN}{title.centre(75)}{RESET}"
    )
    print(
        f"{BLUE}{'=' * 75}{RESET}"
    )

def print_metric(name, value, status=OK):
    print(
        f"{name:<35} : {value:<20} "
        f"[{status_text(status)}]"
    )

# ============================================================
# COMMAND EXECUTION
# ============================================================

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return result.stdout.strip()
        return ""
    except Exception as exc:
        logger.error(
            "Command failed: %s - %s",
            command,
            exc
        )
        return ""

# ============================================================
# SYSTEM INFORMATION
# ============================================================

def get_system_information():
    return{
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_release": platform.release(),
        "kernel": platform.version(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
def display_system_information(data):
    print_header("SYSTEM INFORMATION")
    for key, value in data.items():
        name = key.replace("_", " ").title()
        print(
            f"{name:<35} : {value}"
        )

# ============================================================
# CPU
# ============================================================

def read_cpu_times():
    try:
        with open("/proc/stat", "r") as file:
            line = file.readline()
        values = line.split()

        user = int(values[1])
        nice = int(values[2])
        system = int(values[3])
        idle = int(values[4])
        iowait = int(values[5])
        irq = int(values[6])
        softirq = int(values[7])
        steal = int(values[8])
        idle_time = idle + iowait
        total_time = (
            user
            + nice
            + system
            + idle
            + iowait
            + irq
            + softirq
            + steal
        )
        return total_time, idle_time
    except Exception as exc:
        logger.error(
            "Unable to read CPU statistics: %s",
            exc
        )
        return None, None

def get_cpu_usage():
    total1, idle1 = read_cpu_times()
    if total1 is None:
        return None
    time.sleep(1)
    total2, idle2 = read_cpu_times()
    if total2 is None:
        return None
    total_delta = total2 - total1
    idle_delta = idle2 - idle1
    if total_delta == 0:
        return 0
    usage = (
        total_delta - idle_delta
        / total_delta
    ) * 100
    return round(usage, 2)

def get_cpu_information():
    usage = get_cpu_usage()
    load1, load5, load15 = os.getloadavg()
    cpu_count = os.cpu_count()
    cpu_model = run_command(
        "awk -F': ' '/model name/ {print $2; exit}' "
        "/proc/cpuinfo"
    )
    status = evaluate(
        usage,
        CPU_WARNING,
        CPU_CRITICAL
    )
    return {
        "usage_percent": usage,
        "cores": cpu_count,
        "model": cpu_model,
        "load_1m": round(load1, 2),
        "load_5m": round(load5, 2),
        "load_15m": round(load15, 2),
        "status": status
    }
    
def display_cpu(data):
    print_header("CPU INFORMATION")
    print_metric(
        "CPU Usage",
        f"{data['usage_percent']}%",
        data["status"]
    )
    print(
        f"{'CPU Cores':<35} : {data['cores']}"
    )
    print(
        f"{'CPU Model':<35} : {data['model']}"
    )
    print(
        f"{'Load Average 1m':<35} : "
        f"{data['load_1m']}"
    )
    print(
        f"{'Load Average 5m':<35} : "
        f"{data['load_5m']}"
    )
    print(
        f"{'Load Average 15m':<35} : "
        f"{data['load_15m']}"
    )
    update_overall_status(data["status"])

# ============================================================
# CPU TEMPERATURE
# ============================================================

def get_cpu_temperature():
    temperatures = []
    thermal_path = "/sys/class/thermal"
    if os.path.isdir(thermal_path):
        for entry in os.listdir(thermal_path):
            if not entry.startswith("thermal_zone"):
                continue
            temp_file = os.path.join(
                thermal_path,
                entry,
                "temp"
            )
            try:
                with open(temp_file, "r") as file:
                    value = int(file.read().strip())
                temperature = value / 1000
                if temperature > 0:
                    temperatures.append(
                        temperature
                    )
            except (
                OSError,
                ValueError
            ):
                continue
    # Try hwmon if thermal zones did not provide data
    if not temperatures:
        hwmon_path = "/sys/class/hwmon"
        if os.path.isdir(hwmon_path):
            for hwmon in os.listdir(hwmon_path):
                path = os.path.join(
                    hwmon_path,
                    hwmon
                )
                for filename in os.listdir(path):
                    if (
                        filename.startswith("temp")
                        and filename.endswith("_input")
                    ):
                        temp_file = os.path.join(
                            path,
                            filename
                        )
                        try:
                            with open(
                                temp_file,
                                "r"
                            ) as file:
                                value = int(
                                    file.read().strip()
                                )
                            temperature = value / 1000
                            if temperature > 0:
                                temperatures.append(
                                    temperature
                                )
                        except (
                            OSError,
                            ValueError
                        ):
                            continue
    if not temperatures:
        return None
    return round(max(temperatures), 2)

def display_temperature():
    print_header("CPU TEMPERATURE")
    temperature = get_cpu_temperature()
    if temperature is None:
        print(
            f"{'CPU Temperature':<35} : "
            f"{YELLOW}Not available{RESET}"
        )
        return {
            "temperature_celsius": None,
            "status": UNKNOWN
        }
    status = evaluate(
        temperature,
        TEMP_WARNING,
        TEMP_CRITICAL
    )
    print_metric(
        "CPU Temperature",
        f"{temperature} °C",
        status
    )
    update_overall_status(status)
    return {
        "temperature_celsius": temperature,
        "status": status
    }
# ============================================================
# MEMORY
# ============================================================

def get_memory_information():
    memory = {}
    try:
        with open(
            "/proc/meminfo",
            "r"
        ) as file:
            for line in file:
                key, value = line.split(
                    ":",
                    1
                )
                value = value.strip()
                if value.endswith(" kB"):
                    value = int(
                        value[:-3]
                    ) * 1024
                memory[key] = value
    except Exception as exc:
        logger.error(
            "Unable to read memory information: %s",
            exc
        )
        return None
    total = memory.get(
        "MemTotal",
        0
    )
    available = memory.get(
        "MemAvailable",
        0
    )
    used = total - available
    usage = (
        used / total * 100
        if total
        else 0
    )
    swap_total = memory.get(
        "SwapTotal",
        0
    )
    swap_free = memory.get(
        "SwapFree",
        0
    )
    swap_used = swap_total - swap_free
    swap_usage = (
        swap_used / swap_total * 100
        if swap_total
        else 0
    )
    memory_status = evaluate(
        usage,
        MEMORY_WARNING,
        MEMORY_CRITICAL
    )
    swap_status = evaluate(
        swap_usage,
        SWAP_WARNING,
        SWAP_CRITICAL
    )
    return {
        "total_gb": round(
            total / (1024 ** 3),
            2
        ),
        "used_gb": round(
            used / (1024 ** 3),
            2
        ),
        "available_gb": round(
            available / (1024 ** 3),
            2
        ),
        "usage_percent": round(
            usage,
            2
        ),
        "memory_status": memory_status,
        "swap_total_gb": round(
            swap_total / (1024 ** 3),
            2
        ),
        "swap_usage_percent": round(
            swap_usage,
            2
        ),
        "swap_status": swap_status
    }

# ============================================================
# FILESYSTEM / INODE
# ============================================================

def get_filesystem_information():
    filesystems = []
    output = run_command(
        "df -P -T"
    )
    if not output:
        return filesystems
    lines = output.splitlines()
    for line in lines[1:]:
        fields = line.split()
        if len(fields) < 7:
            continue
        filesystem = fields[0]
        filesystem_type = fields[1]
        try:
            total = int(fields[2])
            used = int(fields[3])
            available = int(fields[4])
        except ValueError:
            continue
        usage = (
            used / total * 100
            if total
            else 0
        )
        mountpoint = " ".join(
            fields[6:]
        )
        filesystems.append({
            "filesystem": filesystem,
            "type": filesystem_type,
            "total_kb": total,
            "used_kb": used,
            "available_kb": available,
            "usage_percent": round(
                usage,
                2
            ),
            "mountpoint": mountpoint
        })
    return filesystems

def get_inode_information():
    inodes = []
    output = run_command(
        "df -P -i"
    )
    if not output:
        return inodes
    lines = output.splitlines()
    for line in lines[1:]:
        fields = line.split()
        if len(fields) < 6:
            continue
        filesystem = fields[0]
        try:
            total = int(fields[1])
            used = int(fields[2])
            available = int(fields[3])
        except ValueError:
            continue
        usage = (
            used / total * 100
            if total
            else 0
        )
        mountpoint = " ".join(
            fields[5:]
        )
        inodes.append({
            "filesystem": filesystem,
            "total": total,
            "used": used,
            "available": available,
            "usage_percent": round(
                usage,
                2
            ),
            "mountpoint": mountpoint
        })
    return inodes

def display_filesystems(filesystems):
    print_header("FILESYSTEM USAGE")
    for filesystem in filesystems:
        usage = filesystem[
            "usage_percent"
        ]
        status = evaluate(
            usage,
            DISK_WARNING,
            DISK_CRITICAL
        )
        size_gb = (
            filesystem["total_kb"]
            / (1024 ** 2)
        )
        used_gb = (
            filesystem["used_kb"]
            / (1024 ** 2)
        )
        print_metric(
            filesystem["mountpoint"],
            f"{used_gb:.2f} / "
            f"{size_gb:.2f} GB "
            f"({usage:.2f}%)",
            status
        )
        update_overall_status(
            status
        )

def display_inodes(inodes):
    print_header("INODE USAGE")
    for inode in inodes:
        usage = inode[
            "usage_percent"
        ]
        status = evaluate(
            usage,
            INODE_WARNING,
            INODE_CRITICAL
        )
        print_metric(
            inode["mountpoint"],
            f"{usage:.2f}%",
            status
        )
        update_overall_status(
            status
        )

# ============================================================
# DISK I/O
# ============================================================

def read_diskstats():
    disks = {}
    try:
        with open(
            "/proc/diskstats",
            "r"
        ) as file:
            for line in file:
                fields = line.split()
                if len(fields) < 14:

                    continue
                device = fields[2]
                # Ignore loop, ram and optical devices
                if (
                    device.startswith("loop")
                    or device.startswith("ram")
                    or device.startswith("sr")
                ):
                    continue
                reads_completed = int(
                    fields[3]
                )
                sectors_read = int(
                    fields[5]
                )
                writes_completed = int(
                    fields[7]
                )
                sectors_written = int(
                    fields[9]
                )
                disks[device] = {
                    "reads": reads_completed,
                    "sectors_read": sectors_read,
                    "writes": writes_completed,
                    "sectors_written":
                        sectors_written

                }

    except Exception as exc:
        logger.error(
            "Unable to read disk statistics: %s",
            exc
        )
    return disks
def get_disk_io():
    first = read_diskstats()
    time.sleep(1)
    second = read_diskstats()
    result = {}
    for device in second:
        if device not in first:
            continue
        read_delta = (
            second[device]["sectors_read"]
            - first[device]["sectors_read"]
        )
        write_delta = (
            second[device]["sectors_written"]
            - first[device]["sectors_written"]
        )
        # Linux sectors are normally 512 bytes
        read_bytes = read_delta * 512
        write_bytes = write_delta * 512
        result[device] = {
            "read_mb_per_sec": round(
                read_bytes / (1024 ** 2),
                2
            ),
            "write_mb_per_sec": round(
                write_bytes / (1024 ** 2),
                2
            )
        }
    return result
def display_disk_io(data):
    print_header("DISK I/O")
    if not data:
        print(
            f"{YELLOW}Disk I/O information unavailable"
            f"{RESET}"
        )
        return
    for device, values in data.items():
        print(
            f"{device:<15} "
            f"Read: "
            f"{values['read_mb_per_sec']} MB/s    "
            f"Write: "
            f"{values['write_mb_per_sec']} MB/s"
        )

#=============================================================
# NETWORK
# ============================================================

def read_network_statistics():
    interfaces = {}
    network_path = (
        "/sys/class/net"
    )
    try:
        for interface in os.listdir(
            network_path
        ):
            if interface == "lo":

                continue
            base = os.path.join(
                network_path,
                interface,
                "statistics"
            )
            with open(
                os.path.join(
                    base,
                    "rx_bytes"
                ),
                "r"
            ) as file:
                rx_bytes = int(
                    file.read()
                )
            with open(
                os.path.join(
                    base,
                    "tx_bytes"
                ),
                "r"
            ) as file:

                tx_bytes = int(
                    file.read()
                )
            interfaces[interface] = {
                "rx_bytes": rx_bytes,
                "tx_bytes": tx_bytes
            }
    except Exception as exc:
        logger.error(
            "Unable to read network statistics: %s",
            exc
        )
    return interfaces
def get_network_statistics():
    first = read_network_statistics()
    time.sleep(1)
    second = read_network_statistics()
    result = {}
    for interface in second:
        if interface not in first:
            continue
        rx_delta = (
            second[interface]["rx_bytes"]
            - first[interface]["rx_bytes"]
        )
        tx_delta = (
            second[interface]["tx_bytes"]
            - first[interface]["tx_bytes"]
        )
        result[interface] = {
            "rx_mb_per_sec": round(
                rx_delta / (1024 ** 2),
                2
            ),
            "tx_mb_per_sec": round(
                tx_delta / (1024 ** 2),
                2
            )
        }
    return result
def display_network(data):
    print_header("NETWORK TRAFFIC")
    if not data:
        print(
            f"{YELLOW}Network statistics unavailable"
            f"{RESET}"
        )
        return
    for interface, values in data.items():
        print(
            f"{interface:<15} "
            f"RX: "
            f"{values['rx_mb_per_sec']} MB/s    "
            f"TX: "
            f"{values['tx_mb_per_sec']} MB/s"
        )

# ============================================================
# PROCESS INFORMATION
# ============================================================

def get_process_information():
    process_count = run_command(
        "ps -e --no-headers | wc -l"
    )
    try:
        process_count = int(
            process_count
        )
    except ValueError:
        process_count = 0
    top_cpu = run_command(
        "ps -eo pid,user,%cpu,%mem,comm "
        "--sort=-%cpu | head -6"
    )
    top_memory = run_command(
        "ps -eo pid,user,%cpu,%mem,comm "
        "--sort=-%mem | head -6"
    )
    return {
        "process_count": process_count,
        "top_cpu": top_cpu,
        "top_memory": top_memory
    }
def display_process_information(data):
    print_header("PROCESS INFORMATION")
    print(
        f"{'Process Count':<35} : "
        f"{data['process_count']}"
    )
    print(
        f"\n{CYAN}Top CPU Processes:{RESET}"
    )
    print(
        data["top_cpu"]
    )
    print(
        f"\n{CYAN}Top Memory Processes:{RESET}"
    )
    print(
        data["top_memory"]
    )


# ============================================================
# UPTIME
# ============================================================

def get_uptime():
    try:
        with open(
            "/proc/uptime",
            "r"
        ) as file:
            seconds = float(
                file.readline().split()[0]
            )
        days = int(
            seconds // 86400
        )
        hours = int(
            (seconds % 86400) // 3600
        )
        minutes = int(
            (seconds % 3600) // 60
        )
        return (
            f"{days}d "
            f"{hours}h "
            f"{minutes}m"
        )

    except Exception:
        return "Unknown"

# ============================================================
# JSON REPORT
# ============================================================

def write_json_report(data, filename):
    try:
        with open(
            filename,
            "w"
        ) as file:
            json.dump(
                data,
                file,
                indent=4
            )
        logger.info(
            "JSON report written to %s",
            filename
        )
    except Exception as exc:
        logger.error(
            "Unable to write JSON report: %s",
            exc
        )

# ============================================================
# EMAIL ALERT
# ============================================================

def send_email_alert(
    smtp_server,
    smtp_port,
    smtp_user,
    smtp_password,
    sender,
    recipient,
    subject,
    body
):

    try:
        message = EmailMessage()
        message["From"] = sender
        message["To"] = recipient
        message["Subject"] = subject
        message.set_content(body)
        with smtplib.SMTP(
            smtp_server,
            smtp_port,
            timeout=20
        ) as server:
            server.starttls()
            if smtp_user:
                server.login(
                    smtp_user,
                    smtp_password
                )
            server.send_message(
                message
            )
        logger.info(
            "Email alert sent to %s",
            recipient
        )
        return True
    except Exception as exc:
        logger.error(
            "Email alert failed: %s",
            exc
        )
        return False


# ============================================================
# ARGUMENTS
# ============================================================

def parse_arguments():
    parser = argparse.ArgumentParser(
        description=(
            "Linux Server Health Monitoring Tool"
        )
    )
    parser.add_argument(
        "--log-file",
        default=DEFAULT_LOG_FILE,
        help="Log file path"
    )
    parser.add_argument(
        "--json-file",
        default=DEFAULT_JSON_FILE,
        help="JSON report path"
    )
    parser.add_argument(
        "--email",
        action="store_true",
        help="Send email when status is WARNING/CRITICAL"
    )
    parser.add_argument(
        "--smtp-server",
        help="SMTP server"
    )
    parser.add_argument(
        "--smtp-port",
        type=int,
        default=587,
        help="SMTP port"
    )
    parser.add_argument(
        "--smtp-user",
        default="",
        help="SMTP username"
    )
    parser.add_argument(
        "--smtp-password",
        default="",
        help="SMTP password"
    )
    parser.add_argument(
        "--sender",
        help="Email sender"
    )
    parser.add_argument(
        "--recipient",
        help="Email recipient"
    )
    return parser.parse_args()

# ============================================================
# MAIN
# ============================================================

def main():
    global overall_status
    args = parse_arguments()
    setup_logging(
        args.log_file
    )
    start_time = time.time()
    timestamp = datetime.now().isoformat()
    logger.info(
        "Starting server health check"
    )

    # --------------------------------------------------------
    # Collect information
    # --------------------------------------------------------

    system = get_system_information()
    cpu = get_cpu_information()
    temperature = display_temperature()
    memory = get_memory_information()
    filesystems = get_filesystem_information()
    inodes = get_inode_information()
    disk_io = get_disk_io()
    network = get_network_statistics()
    processes = get_process_information()
    uptime = get_uptime()
    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    display_system_information(
        system
    )
    display_cpu(
        cpu
    )

    # Temperature status was already evaluated
    # by display_temperature()

    if memory:
        display_memory(
            memory
        )
    display_filesystems(
        filesystems
    )
    display_inodes(
        inodes
    )
    display_disk_io(
        disk_io
    )
    display_network(
        network
    )
    display_process_information(
        processes
    )
    print_header("SYSTEM UPTIME")
    print(
        f"{'Uptime':<35} : {uptime}"
    )
    # --------------------------------------------------------
    # Build JSON
    # --------------------------------------------------------

    report = {
        "timestamp": timestamp,
        "hostname": system["hostname"],
        "overall_status": overall_status,
        "overall_status_text": (
            "OK"
            if overall_status == OK
            else "WARNING"
            if overall_status == WARNING
            else "CRITICAL"
            if overall_status == CRITICAL
            else "UNKNOWN"
        ),
        "system": system,
        "cpu": cpu,
        "temperature": temperature,
        "memory": memory,
        "filesystems": filesystems,
        "inodes": inodes,
        "disk_io": disk_io,
        "network": network,
        "processes": processes,
        "uptime": uptime,
        "execution_time_seconds":
            round(
                time.time() - start_time,
                2
            )
    }
    write_json_report(
        report,
        args.json_file
    )

    # --------------------------------------------------------
    # Final status
    # --------------------------------------------------------

    print_header("FINAL HEALTH STATUS")
    print(
        f"Overall Server Status: "
        f"{status_text(overall_status)}"
    )
    print(
        f"JSON Report         : "
        f"{args.json_file}"
    )
    print(
        f"Log File            : "
        f"{args.log_file}"
    )
    logger.info(
        "Health check completed. Status=%s",
        report["overall_status_text"]
    )

    # --------------------------------------------------------
    # Email alert
    # --------------------------------------------------------

    if (
        args.email
        and overall_status
        in (WARNING, CRITICAL)
        ):
        if not all([
            args.smtp_server,
            args.sender,
            args.recipient
        ]):
            print(
                f"{YELLOW}"
                "WARNING: Email requested but "
                "SMTP configuration is incomplete."
                f"{RESET}"
            )
        else:
            subject = (
                f"[{report['overall_status_text']}] "
                f"Server Health Alert - "
                f"{system['hostname']}"
            )
            body = (
                f"Server Health Alert\n"
                f"===================\n\n"
                f"Hostname : "
                f"{system['hostname']}\n"
                f"Status   : "
                f"{report['overall_status_text']}\n"
                f"Time     : "
                f"{timestamp}\n\n"
                f"CPU      : "
                f"{cpu['usage_percent']}%\n"
                f"Memory   : "
                f"{memory['usage_percent']}%\n"
                f"Swap     : "
                f"{memory['swap_usage_percent']}%\n"
                f"Uptime   : "
                f"{uptime}\n\n"
                f"See JSON report:\n"
                f"{args.json_file}\n"
            )
            send_email_alert(
                args.smtp_server,
                args.smtp_port,
                args.smtp_user,
                args.smtp_password,
                args.sender,
                args.recipient,
                subject,
                body
            )
    print()
    return overall_status

main()



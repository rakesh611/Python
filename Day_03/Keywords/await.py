# await
# Waits for an asynchronous operation.
# Example:
import asyncio

async def check_server():
    await asyncio.sleep(2)
    print("Server checked")

asyncio.run(check_server())

# DevOps use cases include:
# API calls
# Kubernetes API
# Cloud APIs
# SSH/network operations
# Monitoring systems
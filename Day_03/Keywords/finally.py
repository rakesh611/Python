# finally
# Runs whether an exception occurs or not.
try:
    print("Connecting to server")

except Exception:
    print("Connection failed")

finally:
    print("Closing connection")

# Useful for cleanup.
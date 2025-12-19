import socket
import time
from datetime import datetime

def port_scan(target: str):

    # Maximum allowed scan time (seconds)
    # This prevents the scan from running forever
    MAX_SCAN_TIME = 60
    startTime = time.time()

    # Port counter (we will scan from port 0 to 65534)
    portC = 0

    # List to keep track of open ports found
    openPorts = []

    # Log file name (one log per target)
    log_filename = f"scan_{target}.log"

    # Open the log file ONCE (efficient and safe)
    # "w" mode overwrites the file if it already exists
    with open(log_filename, "w") as log:

        # Write scan metadata
        log.write(f"Port scan results for {target}\n")
        log.write(f"Started at: {datetime.now()}\n")
        log.write("-" * 40 + "\n")

        # Main scanning loop
        while portC < 65535:

            # Stop scanning if we exceed the maximum scan time
            if time.time() - startTime > MAX_SCAN_TIME:
                print("\nScan time limit reached")
                log.write("Scan time limit reached\n")
                break

            # Create a TCP socket (IPv4 + TCP)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set a timeout so connect_ex() does not block forever
            # If no response is received within 0.5 seconds,
            # the OS will return a timeout-related error code
            sock.settimeout(0.5)

            # Try to connect to the target and port
            # connect_ex() returns an integer status code instead of raising exceptions
            status = sock.connect_ex((target, portC))

            # Timestamp for log entries
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # status == 0
            # The TCP handshake completed successfully
            # → the port is OPEN
            if status == 0:
                print(f"Port {portC}: OPEN")      # Terminal: only open ports
                openPorts.append(portC)           # Save open port
                log.write(f"[{timestamp}] Port {portC:<5} -> OPEN\n")

            # status == 111 (ECONNREFUSED)
            # The host actively rejected the connection with a TCP RST
            # → the port is CLOSED
            elif status == 111:
                log.write(f"[{timestamp}] Port {portC:<5} -> CLOSED\n")

            # status == 110 (ETIMEDOUT)
            # No reply was received within the timeout
            # Usually means a firewall silently dropped the packet
            # → the port is FILTERED
            elif status == 110:
                log.write(f"[{timestamp}] Port {portC:<5} -> FILTERED (timeout)\n")

            # status == 11 (EAGAIN / EWOULDBLOCK)
            # The OS could not complete the connection immediately
            # due to temporary resource limits or socket exhaustion
            # → result is indeterminate, treated as FILTERED
            elif status == 11:
                log.write(f"[{timestamp}] Port {portC:<5} -> FILTERED (would block)\n")

            # Any other error code
            # These are uncommon but should still be logged
            else:
                log.write(f"[{timestamp}] Port {portC:<5} -> ERROR ({status})\n")

            # Always close the socket to free system resources
            sock.close()

            # Move to the next port
            portC += 1

        # Write scan summary
        log.write("-" * 40 + "\n")
        log.write(f"Open ports: {openPorts}\n")

    # Final terminal message if no open ports were found
    if len(openPorts) == 0:
        print("No open ports found")

    print(f"\nFull scan log saved to: {log_filename}")

def main():
    # Ask the user for the target IP address
    target = input("IP to scan: ")

    # Start the port scan
    port_scan(target)

# Standard Python entry point check
if __name__ == "__main__":
    main()


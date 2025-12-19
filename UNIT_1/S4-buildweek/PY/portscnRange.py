import socket
from datetime import datetime

def port_scan(target: str, portRange: str):

    # Parse the port range string (example: "20-100")
    minPort = int(portRange.split('-')[0])
    maxPort = int(portRange.split('-')[1])

    print(f"Scanning IP {target} from port {minPort} to {maxPort}")

    # List to store open ports
    openPorts = []

    # Log file name (saved in the current working directory)
    log_filename = f"scan_{target}_{minPort}-{maxPort}.log"

    # Open the log file once
    with open(log_filename, "w") as log:

        # Write log header
        log.write(f"Port scan results for {target}\n")
        log.write(f"Port range: {minPort}-{maxPort}\n")
        log.write(f"Started at: {datetime.now()}\n")
        log.write("-" * 40 + "\n")

        # Scan each port in the given range
        for port in range(minPort, maxPort + 1):

            # Create a TCP socket (IPv4, TCP)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Optional but recommended: avoid blocking forever
            sock.settimeout(0.5)

            # Attempt TCP connection
            # connect_ex() returns an OS error code
            status = sock.connect_ex((target, port))

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # status == 0 → OPEN
            if status == 0:
                print(f"Port {port}: OPEN")  # Terminal output
                openPorts.append(port)
                log.write(f"[{timestamp}] Port {port:<5} -> OPEN\n")

            # status == 111 → CLOSED (ECONNREFUSED)
            elif status == 111:
                log.write(f"[{timestamp}] Port {port:<5} -> CLOSED\n")

            # status == 110 → FILTERED (timeout)
            elif status == 110:
                log.write(f"[{timestamp}] Port {port:<5} -> FILTERED (timeout)\n")

            # status == 11 → FILTERED / WOULD BLOCK
            elif status == 11:
                log.write(f"[{timestamp}] Port {port:<5} -> FILTERED (would block)\n")

            # Any other error
            else:
                log.write(f"[{timestamp}] Port {port:<5} -> ERROR ({status})\n")

            # Always close the socket
            sock.close()

        # Write scan summary
        log.write("-" * 40 + "\n")
        log.write(f"Open ports: {openPorts}\n")

    # Final terminal summary
    if len(openPorts) == 0:
        print("No open ports found")

    print(f"\nFull scan log saved to: {log_filename}")

def main():
    target = input("IP to scan: ")
    portRange = input("Ports range (Es. 20-100): ")

    port_scan(target, portRange)

if __name__ == "__main__":
    main()

import socket
import time

target = input("IP to scan: ")

MAX_SCAN_TIME = 60 
startTime = time.time()

portC = 0
openPorts = []

while portC < 65535:

    if time.time() - startTime > MAX_SCAN_TIME:
        print("\n Scan time limit reached")
        break

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    status = sock.connect_ex((target, portC))

    if status == 0 :
        print(f"Port {portC}: OPEN")
        openPorts.append(portC)
        sock.close()
    elif status != 111:
        print(status,portC)
        sock.close()
    else:
        sock.close()

    portC += 1
        
if len(openPorts) == 0:
    print("No open ports found")
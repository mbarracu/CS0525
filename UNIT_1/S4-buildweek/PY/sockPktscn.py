import socket
import struct
import os
import sys

def require_root():
    if os.geteuid() != 0:
        print("[!] Raw sockets require root privileges.")
        sys.exit(1)

def get_default_interface() -> str:
    """
    Return the first non-loopback interface.
    Suitable for single-interface lab environments.
    """
    for _, iface in socket.if_nameindex():
        if iface != "lo":
            return iface
    raise RuntimeError("No suitable network interface found")


def capture_packets_for_ip(target_ip: str, max_packets: int = 10):
    interface = get_default_interface()

    sock = socket.socket(
        socket.AF_PACKET,
        socket.SOCK_RAW,
        socket.ntohs(0x0003)
    )

    sock.bind((interface, 0))

    print(f"[+] Using interface: {interface}")
    print(f"[+] Filtering packets for IP: {target_ip}\n")

    captured = 0

    while captured < max_packets:
        raw_data, _ = sock.recvfrom(65535)

        eth_proto = struct.unpack("!H", raw_data[12:14])[0]

        if eth_proto == 0x0800:  # IPv4
            ip_header = raw_data[14:34]
            iph = struct.unpack("!BBHHHBBH4s4s", ip_header)

            src_ip = socket.inet_ntoa(iph[8])
            dst_ip = socket.inet_ntoa(iph[9])

            if src_ip == target_ip or dst_ip == target_ip:
                captured += 1
                print(f"Packet {captured}")
                print(f"  Source IP      : {src_ip}")
                print(f"  Destination IP : {dst_ip}")
                print(f"  Length         : {len(raw_data)} bytes\n")

    sock.close()
    print("[+] Capture complete")

def main():
    require_root()
    target_ip = input("Target IP to filter: ").strip()
    capture_packets_for_ip(target_ip)


if __name__ == "__main__":
    main()

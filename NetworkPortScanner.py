import socket
import threading
from queue import Queue

def check_port(ip, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout()  # Set a timeout for the connection attempt

    try:
        # Attempt to connect to the specified IP address and port
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def scan_ports(ip):
    # Scan a range of ports for the given IP address
    for port in range(1, 1001):  # Scan ports from 1 to 1000
        check_port(ip, port)

def scan_ips(ips):
    # Scan a range of IP addresses using multiple threads
    for ip in ips:
        # Create a new thread for each IP address
        t = threading.Thread(target=scan_ports, args=(ip,))
        t.start()

def split_ip_range(ip_range):
    # Split the IP range into individual IP addresses
    start_ip, end_ip = ip_range.split("-")
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    ips = []

    while start != end:
        ips.append(".".join(map(str, start)))
        start[3] += 1
        for i in (3, 2, 1):
            if start[i] == 256:
                start[i] = 0
                start[i - 1] += 1

    ips.append(".".join(map(str, end)))
    return ips

def main():
    # Get the IP range to scan from the user
    ip_range = input("Enter IP range to scan (e.g., 192.168.0.1-192.168.0.10): ")
    ips = split_ip_range(ip_range)

    # Scan the IP addresses
    scan_ips(ips)

if __name__ == "__main__":
    main()

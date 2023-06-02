# NetworkPortScanner
A python network port scanner that allows users to scan a range of IP addresses and ports to check for open or closed ports. The program can provide information about the status of each port and can be helpful in identifying potential vulnerabilities in a network.

Main Methods Used:
check_port(ip, port)- to create a socket object and attempt to connect to the specified IP address and port. It checks if the port is open or closed and prints the result.

scan_ports(ip)- to scan a range of ports (from 1 to 1000) for the given IP address. It calls check_port for each port.

scan_ips(ips)- to scan a range of IP addresses using multiple threads. It creates a new thread for each IP address and calls scan_ports.

split_ip_range(ip_range)- to split the given IP range into individual IP addresses. It converts the start and end IP addresses into lists of integers, increments the IP addresses in a loop, and creates a list of IP addresses.

main()- to get the IP range to scan from the user and splits it into individual IP addresses. It then calls scan_ips to initiate the scanning process.



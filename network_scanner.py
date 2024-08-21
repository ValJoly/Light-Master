import socket

def get_ip_address(hostname):
    try:
        # Get the IP address for the given hostname
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address of the hostname: {hostname} is {ip_address}")
        return ip_address
    except socket.gaierror:
        # Handle the exception if the hostname is invalid
        print(f"Invalid hostname: {hostname}")
        return ""


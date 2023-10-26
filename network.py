import sys
import psutil
import socket
import os

def lookup(domain_name):
    try:
        ip = socket.gethostbyname(domain_name)
        return ip
    except socket.gaierror:
        return f"'{domain_name}' is not an available domain."

def ping(ip):
    response = os.system("ping -n 1 " + ip)
    if response == 0:
        return "UP !"
    else:
        return "DOWN !"

def get_wifi_ip():
    wifi_interface = [iface for iface, addrs in psutil.net_if_addrs().items() if "Wi-Fi" in iface]
    if wifi_interface:
        wifi_ip = [addr.address for iface, addrs in psutil.net_if_addrs().items() if "Wi-Fi" in iface for addr in addrs if addr.family == socket.AF_INET][0]
        return wifi_ip
    else:
        return "Wi-Fi not found."

def main():
    if len(sys.argv) < 2:
        print("Usage: python network.py [lookup|ping|ip] [domain_name|ip_address]")
        return

    command = sys.argv[1]

    if command == "lookup":
        if len(sys.argv) < 3:
            print("Usage: python network.py lookup [domain_name]")
            return
        domain_name = sys.argv[2]
        result = lookup(domain_name)

    elif command == "ping":
        if len(sys.argv) < 3:
            print("Usage: python network.py ping [ip_address]")
            return
        ip_address = sys.argv[2]
        result = ping(ip_address)

    elif command == "ip":
        result = get_wifi_ip()

    else:
        result = f"'{command}' is not an available command. Déso."

    print(result)

if __name__ == "__main__":
    main()

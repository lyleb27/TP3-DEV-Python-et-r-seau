import socket
import sys

def lookup_domain(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"L'adresse IP de {domain_name} est {ip_address}")
    except socket.gaierror:
        print(f"Impossible de résoudre l'adresse IP de {domain_name}")

if len(sys.argv) < 2:
    print("Usage: python lookup.py <domain_name>")
else:
    domain_name = sys.argv[1]
    lookup_domain(domain_name)

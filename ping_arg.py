from sys import argv
import os

if len(argv) < 1:
    print("Usage: python ping_arg.py <8.8.8.8>")
else:
    ip_address = argv[1]
    os.system(f"ping {ip_address}")


from sys import argv
import subprocess
import sys

if len(argv) < 1:
    print("Utilisation : python is_up.py <adresse_ip>")
else:
    adresse_ip = sys.argv[1]
    commande_ping = f"ping -n 1 {adresse_ip}" 
    result = subprocess.run(commande_ping, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("UP !")
    else:
        print("DOWN !")

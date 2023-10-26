import psutil; 
print([addr.address for iface, addrs in psutil.net_if_addrs().items() if "Wi-Fi" in iface for addr in addrs if addr.family == 2][0])




# ICMP-Flood-Attack-Simulation
import sys
print(sys.executable)
from scapy.all import *

target_ip = ""  # Replace with your IP address

print("Sending high-volume ping requests...")
for i in range(500):  # Adjust the number of packets
    send(IP(dst=target_ip)/ICMP())
print("Finished sending requests.")

#ICMP-Flood-Attack-Detection
import pyshark
from collections import defaultdict
#Threshold for number of ICMP requests from one IP
THRESHOLD = 100

def analyze_pcap(pcap_file):
    capture = pyshark.FileCapture(pcap_file, display_filter="icmp", keep_packets=False)
    packet_counts = defaultdict(int)
    total_packets = 0

    print("Analyzing ICMP traffic...")

    for packet in capture:
        total_packets += 1
        try:
            src_ip = packet.ip.src
            packet_counts[src_ip] += 1
        except AttributeError:
            continue

    capture.close()

    print(f"Total packets analyzed: {total_packets}")
    for ip, count in packet_counts.items():
        print(f"{ip}: {count} packets")
        if count > THRESHOLD:
            print(f"ALERT: Potential ICMP Flood attack detected from {ip}! ({count} packets)")

analyze_pcap("/path/to/pcap/file")

from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):  # Captures only IP packets
        if packet.haslayer("TCP"):  # Check for TCP layer
            print(f"Source: {packet['IP'].src} --> Destination: {packet['IP'].dst} | Protocol: TCP")
        elif packet.haslayer("UDP"):  # Check for UDP layer
            print(f"Source: {packet['IP'].src} --> Destination: {packet['IP'].dst} | Protocol: UDP")

# Sniff network packets (captures only 6 packets)
print("Sniffing started... Press Ctrl+C to stop.")
sniff(prn=packet_callback, count=6)
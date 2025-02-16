### What This Code Does 

This Python script uses the `scapy` library to capture and analyze network packets. Here's a breakdown of its functionality:

1. **Packet Sniffing**:
   - The script captures network packets passing through the system's network interface.
   - It uses the `sniff` function from the `scapy` library to perform this task.

2. **Filtering IP Packets**:
   - The script checks if the captured packets have an **IP layer**. If they do, it proceeds to analyze them further.

3. **Identifying TCP and UDP Packets**:
   - If the packet has a **TCP layer**, it prints the source IP address, destination IP address, and the protocol (TCP).
   - If the packet has a **UDP layer**, it prints the source IP address, destination IP address, and the protocol (UDP).

4. **Limiting the Number of Packets**:
   - The script is configured to capture only **6 packets** (as specified by the `count=6` parameter in the `sniff` function).

5. **Output**:
   - For each captured packet, the script prints details like:
     - **Source IP**: The IP address from which the packet originated.
     - **Destination IP**: The IP address to which the packet is being sent.
     - **Protocol**: Whether the packet uses TCP or UDP.

6. **User Interaction**:
   - When the script starts, it prints: `"Sniffing started... Press Ctrl+C to stop."` to inform the user that packet capture has begun.
   - The user can stop the script by pressing `Ctrl+C`.

---

### Example Output:
If the script captures a TCP packet, the output might look like this:
```
Source: 192.168.1.100 --> Destination: 192.168.1.1 | Protocol: TCP
```

If it captures a UDP packet, the output might look like this:
```
Source: 192.168.1.100 --> Destination: 192.168.1.2 | Protocol: UDP
```

---

### Use Case:
This script is useful for:
- Monitoring network traffic.
- Debugging network-related issues.
- Learning about network protocols (TCP/UDP) and packet structures.

---

### How to Run:
1. Install the `scapy` library using pip:
   ```bash
   pip install scapy
   ```
2. Run the script:
   ```bash
   python script_name.py
   ```
3. The script will capture and display details of 6 network packets.


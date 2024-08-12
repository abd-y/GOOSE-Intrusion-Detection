from scapy.all import rdpcap, Ether, Raw

def parse_goose_payload(payload):
    # Manually parse the GOOSE fields from the raw payload
    # Adjust offsets based on actual data layout
    goose_data = {}
    
    goose_data['sqNum'] = int.from_bytes(payload[10:12], byteorder='big')
    goose_data['stNum'] = int.from_bytes(payload[12:14], byteorder='big')
    goose_data['timeAllowedtoLive'] = int.from_bytes(payload[14:16], byteorder='big')
    goose_data['goCBRef'] = payload[16:36].decode('ascii', errors='ignore').strip()
    goose_data['datSet'] = payload[36:56].decode('ascii', errors='ignore').strip()
    goose_data['goID'] = payload[56:76].decode('ascii', errors='ignore').strip()
    for i in payload:
        try:
            int.from_bytes(i, byteorder='big')
        except Exception as e:
            print(e)
        continue
    # This example assumes fixed field lengths and byte offsets.
    # You'll need to adjust these based on your GOOSE message structure.
    return goose_data

# Read the PCAP file
packets = rdpcap('Sample_File_GOOSE.pcap')

# Loop through all packets and filter for GOOSE packets
goose_packets = []
for pkt in packets:
    if Ether in pkt and pkt[Ether].type == 33024:  # 0x88b8 is the EtherType for GOOSE
        goose_packets.append(pkt)

# Extract and print details from GOOSE packets
for i, pkt in enumerate(goose_packets, 1):
    if Raw in pkt:
        goose_payload = bytes(pkt[Raw].load)
        goose_data = parse_goose_payload(goose_payload)
    
        print(f"GOOSE Packet {i}:")
        print(f"Source MAC: {pkt[Ether].src}")
        print(f"Destination MAC: {pkt[Ether].dst}")
        print(f"Sequence Number (sqNum): {goose_data['sqNum']}")
        print(f"State Number (stNum): {goose_data['stNum']}")
        print(f"Time Allowed to Live: {goose_data['timeAllowedtoLive']}")
        print(f"GOCB Reference (goCBRef): {goose_data['goCBRef']}")
        print(f"Data Set (datSet): {goose_data['datSet']}")
        print(f"GOOSE ID (goID): {goose_data['goID']}")
        print("\n")
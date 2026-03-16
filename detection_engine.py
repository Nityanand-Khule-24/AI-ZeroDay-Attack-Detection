import joblib
import numpy as np
from scapy.all import sniff, IP, TCP, UDP

model = joblib.load("attack_type_model.pkl")

print("Advanced AI Model Loaded")
print("Detecting attack types...")

def process_packet(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        packet_len = len(packet)

        protocol = 0
        if packet.haslayer(TCP):
            protocol = 1
        elif packet.haslayer(UDP):
            protocol = 2

        features = np.array([[packet_len, protocol, 1, 1, 1, packet_len/2, packet_len/4]])

        attack_type = model.predict(features)[0]

        if attack_type == "BENIGN":

            print("✅ Normal Traffic")

        else:

            print("🚨 ATTACK DETECTED")
            print("Type:", attack_type)

        print("Source:", src, "→ Target:", dst)
        print("----------------------------------")

sniff(prn=process_packet)
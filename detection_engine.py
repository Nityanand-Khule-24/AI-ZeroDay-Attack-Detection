import joblib
import numpy as np
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time
import os
from datetime import datetime

# ===== LOAD MODEL =====
model = joblib.load("attack_type_model.pkl")

print("✅ Advanced AI Model Loaded")
print("🚀 Detecting attack types...\n")

# ===== CSV FILE =====
LOG_FILE = "attack_logs.csv"

# Create CSV if not exists
if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=[
        "Time", "Source IP", "Destination IP",
        "Packet Length", "Protocol",
        "Status", "Attack Type"
    ])
    df.to_csv(LOG_FILE, index=False)

# ===== SAFE CSV WRITE FUNCTION =====
def safe_write_csv(row, file):
    for _ in range(5):  # retry multiple times
        try:
            row.to_csv(file, mode='a', header=False, index=False)
            break
        except:
            time.sleep(0.1)

# ===== TRACK TRAFFIC =====
packet_count = defaultdict(int)
start_time = time.time()


def process_packet(packet):

    global packet_count, start_time

    if packet.haslayer(IP):

        try:
            src = packet[IP].src
            dst = packet[IP].dst
            packet_len = len(packet)

            # ===== PROTOCOL =====
            protocol = 0
            if packet.haslayer(TCP):
                protocol = 1
            elif packet.haslayer(UDP):
                protocol = 2

            # ===== AI FEATURES =====
            features = np.array([[packet_len, protocol, 1, 1, 1, packet_len/2, packet_len/4]])
            attack_type = model.predict(features)[0]

            # ===== COUNT PACKETS =====
            packet_count[src] += 1

            # ===== RULE DETECTION =====
            suspicious = False

            if packet_len > 1200:
                suspicious = True

            if protocol == 2 and packet_len > 800:
                suspicious = True

            if packet_count[src] > 20:
                suspicious = True

            # reset every 10 sec
            if time.time() - start_time > 10:
                packet_count.clear()
                start_time = time.time()

            # ===== FINAL STATUS =====
            if attack_type != "BENIGN" or suspicious:
                status = "Suspicious"
                print("🚨 SUSPICIOUS / ATTACK TRAFFIC")
                print("AI Type:", attack_type)
            else:
                status = "Normal"
                print("✅ Normal Traffic")

            print("Source:", src, "→ Target:", dst)
            print("Packet Length:", packet_len)
            print("----------------------------------")

            # ===== SAVE TO CSV =====
            new_row = pd.DataFrame([{
                "Time": datetime.now(),
                "Source IP": src,
                "Destination IP": dst,
                "Packet Length": packet_len,
                "Protocol": protocol,
                "Status": status,
                "Attack Type": attack_type
            }])

            safe_write_csv(new_row, LOG_FILE)

        except Exception as e:
            print("❌ Error:", e)


# ===== START SNIFFING =====
sniff(prn=process_packet, store=False)
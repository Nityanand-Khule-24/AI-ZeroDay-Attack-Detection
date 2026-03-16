import streamlit as st
import pandas as pd
import requests
import ipaddress
from streamlit_autorefresh import st_autorefresh

# ===== PAGE SETTINGS =====
st.set_page_config(page_title="AI Cyber Attack Detection", layout="wide")

# auto refresh every 5 seconds
st_autorefresh(interval=5000, key="datarefresh")

st.title("🛡 AI Zero-Day Cyber Attack Detection Dashboard")

# ===== LOAD DATA =====
try:
    data = pd.read_csv("attack_logs.csv")
except:
    st.warning("Waiting for traffic data...")
    st.stop()

# ===== TOP METRICS =====
normal_count = len(data[data["Status"] == "Normal"])
attack_count = len(data[data["Status"] == "Suspicious"])
total_packets = len(data)

col1, col2, col3 = st.columns(3)

col1.metric("Total Packets", total_packets)
col2.metric("Normal Traffic", normal_count)
col3.metric("Suspicious Traffic", attack_count)

st.markdown("---")

# ===== TRAFFIC DISTRIBUTION =====
st.subheader("📊 Traffic Distribution")

traffic_chart = data["Status"].value_counts()
st.bar_chart(traffic_chart)

# ===== PACKET SIZE TREND =====
st.subheader("📈 Packet Length Trend")

st.line_chart(data["Packet Length"])

st.markdown("---")

# ===== NETWORK LOGS =====
st.subheader("📄 Recent Network Logs")

st.dataframe(data.tail(20))

st.markdown("---")

# ===== SUSPICIOUS TRAFFIC TABLE =====
st.subheader("🚨 Suspicious Traffic")

suspicious = data[data["Status"] == "Suspicious"]

if len(suspicious) > 0:
    st.dataframe(suspicious.tail(10))
else:
    st.success("No suspicious traffic detected")

st.markdown("---")

# ===== LIVE ATTACK ALERT =====
if len(suspicious) > 0:

    latest = suspicious.tail(1)

    src = latest["Source IP"].values[0]
    dst = latest["Destination IP"].values[0]

    st.error(f"🚨 LIVE ATTACK ALERT 🚨  \nSource: {src} → Target: {dst}")

st.markdown("---")

# ===== GLOBAL ATTACK MAP =====
st.subheader("🌍 Global Attack Map")

locations = []

all_ips = pd.concat([data["Source IP"], data["Destination IP"]]).unique()

for ip in all_ips:

    try:

        # skip private IPs
        if ip.startswith("10.") or ip.startswith("192.168") or ip.startswith("172."):
            continue

        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json()

        if res["status"] == "success":

            locations.append({
                "lat": res["lat"],
                "lon": res["lon"]
            })

    except Exception as e:
        st.write("Error for IP:", ip)

# DEBUG
st.write("Locations found:", len(locations))

# fallback test point
if len(locations) == 0:
    locations.append({"lat": 37.7749, "lon": -122.4194})

map_df = pd.DataFrame(locations)

st.map(map_df)
import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="AI Cyber Attack Detection",
    page_icon="🛡",
    layout="wide"
)

st.title("🛡 AI Zero-Day Cyber Attack Detection System")
st.markdown("---")

# Load data
data = pd.read_csv("attack_logs.csv")

# ===== TOP METRICS =====
normal_count = len(data[data["Status"] == "Normal"])
attack_count = len(data[data["Status"] == "Suspicious"])
total_packets = len(data)

col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Packets", total_packets)
col2.metric("✅ Normal Traffic", normal_count)
col3.metric("⚠️ Suspicious Traffic", attack_count)

st.markdown("---")

# ===== TRAFFIC CHART =====
st.subheader("📊 Traffic Distribution")

traffic_chart = data["Status"].value_counts()
st.bar_chart(traffic_chart)

st.markdown("---")

# ===== RECENT LOGS =====
st.subheader("📄 Recent Network Logs")

st.dataframe(data.tail(20))

st.markdown("---")

# ===== SUSPICIOUS TRAFFIC =====
st.subheader("🚨 Suspicious Traffic")

suspicious = data[data["Status"] == "Suspicious"]

if len(suspicious) > 0:
    st.dataframe(suspicious.tail(10))
else:
    st.success("No suspicious traffic detected")

st.markdown("---")

# ===== GLOBAL ATTACK MAP =====
st.subheader("🌍 Global Attack Map")

locations = []

for ip in suspicious["Source IP"].unique():

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()

        if res["status"] == "success":
            locations.append({
                "lat": res["lat"],
                "lon": res["lon"]
            })

    except:
        pass

if locations:
    map_df = pd.DataFrame(locations)
    st.map(map_df)
else:
    st.info("No attack locations available")
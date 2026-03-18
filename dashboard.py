import streamlit as st
import pandas as pd
import requests
import ipaddress
from streamlit_autorefresh import st_autorefresh
from auth import login, logout

# ===== LOGIN SYSTEM =====
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    login()
    st.stop()

# ===== PAGE SETTINGS =====
st.set_page_config(page_title="AI Cyber Attack Detection", layout="wide")

# ===== SIDEBAR =====
st.sidebar.title("🛡 Cyber Defense System")
st.sidebar.write("User:", st.session_state.get("user", "Guest"))

page = st.sidebar.selectbox("Navigation", ["Dashboard", "Admin"])

# ===== ADMIN PANEL =====
if page == "Admin":
    import admin
    st.stop()

# ===== DARK THEME =====
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #00ffcc;
}
.stMetric {
    background-color: #111;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ===== AUTO REFRESH =====
st_autorefresh(interval=5000, key="refresh")

# ===== HEADER =====
col1, col2 = st.columns([8,1])

with col1:
    st.title("🛡 AI Zero-Day Cyber Attack Detection Dashboard")

with col2:
    if st.button("Logout"):
        logout()

# ===== LOAD DATA =====
try:
    data = pd.read_csv("attack_logs.csv", on_bad_lines='skip')

    required_cols = ["Time", "Source IP", "Destination IP", "Packet Length", "Status"]

    for col in required_cols:
        if col not in data.columns:
            st.warning("⚠ Waiting for correct data format...")
            st.stop()

except:
    st.warning("⏳ Waiting for traffic data...")
    st.stop()

# ===== CLEAN DATA =====
data = data.dropna()
data["Time"] = pd.to_datetime(data["Time"], errors="coerce")

# ===== METRICS =====
normal_count = len(data[data["Status"] == "Normal"])
attack_count = len(data[data["Status"] == "Suspicious"])
total_packets = len(data)

col1, col2, col3 = st.columns(3)

col1.metric("📦 Total Packets", total_packets)
col2.metric("✅ Normal Traffic", normal_count)
col3.metric("🚨 Suspicious Traffic", attack_count)

st.markdown("---")

# ===== THREAT LEVEL =====
st.subheader("🎯 Threat Level")

risk = (attack_count / total_packets) * 100 if total_packets > 0 else 0

if risk > 50:
    st.error(f"🔥 HIGH RISK: {risk:.2f}%")
elif risk > 20:
    st.warning(f"⚠ MEDIUM RISK: {risk:.2f}%")
else:
    st.success(f"✅ LOW RISK: {risk:.2f}%")

# ===== AI INSIGHTS =====
st.subheader("🧠 AI Insights")

if len(data) > 0:
    most_common = data["Status"].value_counts().idxmax()
    st.info(f"Most traffic type: {most_common}")

    if attack_count > normal_count:
        st.error("⚠ System under possible attack!")
    else:
        st.success("✅ Network stable")

st.markdown("---")

# ===== TRAFFIC DISTRIBUTION =====
st.subheader("📊 Traffic Distribution")
st.bar_chart(data["Status"].value_counts())

# ===== ATTACK TYPES =====
if "Attack Type" in data.columns:
    st.subheader("🧬 Attack Types")
    st.bar_chart(data["Attack Type"].value_counts())

# ===== TIMELINE =====
st.subheader("📈 Attack Timeline")

timeline = data.groupby(data["Time"].dt.floor("S"))["Status"].count()
st.line_chart(timeline)

st.markdown("---")

# ===== TOP ATTACKERS =====
st.subheader("🔥 Top Attacker IPs")

top_ips = data[data["Status"] == "Suspicious"]["Source IP"].value_counts().head(5)

if not top_ips.empty:
    st.bar_chart(top_ips)
else:
    st.info("No attackers yet")

st.markdown("---")

# ===== LIVE ALERT =====
st.subheader("🚨 Live Alerts")

suspicious = data[data["Status"] == "Suspicious"]

if len(suspicious) > 0:
    latest = suspicious.tail(1)

    src = latest["Source IP"].values[0]
    dst = latest["Destination IP"].values[0]

    st.error(f"""
🚨 LIVE ATTACK DETECTED 🚨  
Source: {src} → Target: {dst}
""")

    # SOUND ALERT
    st.audio("https://www.soundjay.com/buttons/beep-01a.mp3")

else:
    st.success("✅ No live attacks")

st.markdown("---")

# ===== RECENT LOGS =====
st.subheader("📄 Recent Network Logs")
st.dataframe(data.tail(20), use_container_width=True)

st.markdown("---")

# ===== GLOBAL MAP =====
st.subheader("🌍 Global Attack Map")

locations = []

all_ips = pd.concat([data["Source IP"], data["Destination IP"]]).dropna().unique()

for ip in all_ips:
    try:
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:
            continue

        res = requests.get(f"http://ip-api.com/json/{ip}", timeout=3).json()

        if res.get("status") == "success":
            locations.append({
                "lat": res["lat"],
                "lon": res["lon"]
            })

    except:
        continue

# fallback (India)
if len(locations) == 0:
    locations.append({"lat": 20.5937, "lon": 78.9629})

map_df = pd.DataFrame(locations)
st.map(map_df)

# ===== LIVE TRAFFIC SPEED =====
st.subheader("⚡ Live Traffic Speed")
st.metric("Packets / 5 sec", total_packets)

# ===== FOOTER =====
st.markdown("---")
st.caption("⚡ Powered by AI | Real-Time Cyber Defense System")
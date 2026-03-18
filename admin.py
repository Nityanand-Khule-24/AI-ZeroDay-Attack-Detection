import streamlit as st
import pandas as pd

st.title("🛠 Admin Panel")

data = pd.read_csv("attack_logs.csv")

st.subheader("📊 Full Data Access")
st.dataframe(data, use_container_width=True)

st.subheader("🧹 Data Controls")

if st.button("Clear Logs"):
    data.iloc[0:0].to_csv("attack_logs.csv", index=False)
    st.success("Logs Cleared ✅")

st.subheader("📥 Download Logs")

st.download_button(
    label="Download CSV",
    data=data.to_csv(index=False),
    file_name="attack_logs.csv",
    mime="text/csv"
)
import streamlit as st

# simple demo users (you can upgrade later)
USERS = {
    "admin": "admin123",
    "user": "user123"
}

def login():
    st.title("🔐 Login - Cyber Defense System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid Credentials ❌")

def logout():
    st.session_state["logged_in"] = False
    st.rerun()
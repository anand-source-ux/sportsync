import streamlit as st
import pandas as pd

st.title("🎓 Student Login")

users = pd.read_csv("users.csv")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    match = users[
        (users["Username"] == username) &
        (users["Password"] == password) &
        (users["Role"] == "Student")
    ]

    if len(match) > 0:
        st.success("Login Successful")
        st.session_state["student"] = username
    else:
        st.error("Invalid Credentials")
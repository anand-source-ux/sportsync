import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Analytics Dashboard")

bookings = pd.read_csv(
    "bookings.csv"
)

if len(bookings) > 0:

    chart = px.histogram(
        bookings,
        x="Sport"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

attendance = pd.read_csv(
    "attendance.csv"
)

st.subheader(
    "Attendance Records"
)

st.dataframe(attendance)
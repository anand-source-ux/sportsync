import streamlit as st
import pandas as pd

st.title("📱 Attendance")

booking_id = st.text_input(
    "Enter Booking ID"
)

if st.button("Mark Attendance"):

    bookings = pd.read_csv(
        "bookings.csv"
    )

    match = bookings[
        bookings["BookingID"] == booking_id
    ]

    if len(match) > 0:

        attendance = pd.read_csv(
            "attendance.csv"
        )

        row = pd.DataFrame({
            "BookingID":[booking_id],
            "Student":[match.iloc[0]["Student"]],
            "Sport":[match.iloc[0]["Sport"]],
            "Status":["Present"]
        })

        attendance = pd.concat(
            [attendance,row],
            ignore_index=True
        )

        attendance.to_csv(
            "attendance.csv",
            index=False
        )

        st.success("Attendance Marked")

    else:
        st.error("Booking Not Found")
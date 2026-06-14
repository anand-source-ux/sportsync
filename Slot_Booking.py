import streamlit as st
import pandas as pd
from datetime import date
import qrcode

st.title("📅 Slot Booking")

sports = [
    "Gymnasium",
    "Swimming",
    "Basketball",
    "Football",
    "Snooker",
    "Table Tennis",
    "Tennis",
    "Cricket"
]

student = st.text_input("Student Name")

sport = st.selectbox("Sport", sports)

booking_date = st.date_input(
    "Date",
    min_value=date.today()
)

time_slot = st.selectbox(
    "Time",
    [
        "6 AM",
        "7 AM",
        "8 AM",
        "4 PM",
        "5 PM",
        "6 PM"
    ]
)

if st.button("Book Slot"):

    bookings = pd.read_csv("bookings.csv")

    booking_id = f"BK{len(bookings)+1}"

    new_row = pd.DataFrame({
        "BookingID":[booking_id],
        "Student":[student],
        "Sport":[sport],
        "Date":[booking_date],
        "Time":[time_slot]
    })

    bookings = pd.concat(
        [bookings,new_row],
        ignore_index=True
    )

    bookings.to_csv(
        "bookings.csv",
        index=False
    )

    qr = qrcode.make(booking_id)

    qr.save(
        f"qr_codes/{booking_id}.png"
    )

    st.success(
        f"Booking Created: {booking_id}"
    )

    st.image(
        f"qr_codes/{booking_id}.png"
    )
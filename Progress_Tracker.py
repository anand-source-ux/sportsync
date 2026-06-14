import streamlit as st
import pandas as pd

st.title("📈 Progress Tracker")

student = st.text_input(
    "Student Name"
)

sport = st.text_input(
    "Sport"
)

score = st.number_input(
    "Performance Score",
    0,
    100
)

feedback = st.text_area(
    "Coach Feedback"
)

if st.button("Save Progress"):

    progress = pd.read_csv(
        "progress.csv"
    )

    row = pd.DataFrame({
        "Student":[student],
        "Sport":[sport],
        "Score":[score],
        "Feedback":[feedback]
    })

    progress = pd.concat(
        [progress,row],
        ignore_index=True
    )

    progress.to_csv(
        "progress.csv",
        index=False
    )

    st.success(
        "Progress Saved"
    )

st.subheader("Records")

st.dataframe(
    pd.read_csv("progress.csv")
)
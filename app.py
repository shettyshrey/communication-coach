from streamlit_extras.switch_page_button import switch_page
import streamlit as st

st.set_page_config(page_title="AI Communication Coach", layout="centered")

st.title("🧠 Communication Coach")
st.subheader("Practice real-life conversations powered by AI")
st.markdown("Choose your mode:")

mode = st.radio("Select", ["🧑‍🦱 Practice Mode", "🧑‍⚕️ Therapist Dashboard"])

if st.button("Continue"):
    if "Practice" in mode:
        switch_page("1_Patient_Mode")
    else:
        switch_page("2_Therapist_Dashboard")

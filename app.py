import streamlit as st

st.set_page_config(page_title="AI Communication Coach", layout="centered")

st.title("🧠 Communication Coach")
st.subheader("Practice real-life conversations powered by AI")

st.markdown("Choose your mode:")

mode = st.radio("Select", ["🧑 Practice Mode", "🧑‍⚕️ Therapist Dashboard"])

if st.button("Continue"):
    if "Practice" in mode:
        st.switch_page("pages/1_Patient_Mode.py")
    else:
        st.switch_page("pages/2_Therapist_Dashboard.py")

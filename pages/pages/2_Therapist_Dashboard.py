import streamlit as st
import pandas as pd
import datetime

# Simulated data
patients = {
    "Alice Smith": [
        {"date": "2024-07-15", "scenario": "Order Coffee", "accuracy": "92%", "notes": "Minor mispronunciation"},
        {"date": "2024-07-18", "scenario": "Introduce Yourself", "accuracy": "95%", "notes": "Clear and confident"},
    ],
    "John Doe": [
        {"date": "2024-07-14", "scenario": "Call the Doctor", "accuracy": "85%", "notes": "Struggled with phrasing"},
        {"date": "2024-07-20", "scenario": "Order Coffee", "accuracy": "89%", "notes": "Improved clarity"},
    ],
}

st.set_page_config(page_title="Therapist Dashboard", layout="wide")
st.title("🧑‍⚕️ Therapist Dashboard")

# Patient selector
selected_patient = st.selectbox("Select a patient to view their progress:", list(patients.keys()))

# Display practice history
if selected_patient:
    st.subheader(f"📈 Practice History: {selected_patient}")
    
    df = pd.DataFrame(patients[selected_patient])
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date", ascending=False)
    st.table(df)

    st.markdown("---")

    # Assign a new practice
    st.subheader("📝 Assign New Practice Session")
    new_scenario = st.selectbox("Choose a scenario:", ["Order Coffee", "Introduce Yourself", "Call the Doctor"])
    assign_button = st.button("Assign Practice")

    if assign_button:
        st.success(f"New practice scenario '{new_scenario}' assigned to {selected_patient}. (mocked)")

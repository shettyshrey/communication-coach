import streamlit as st

st.title("🧑 Practice Mode")
st.markdown("This is where a patient can practice real-world scenarios like ordering coffee, introducing themselves, or calling a doctor.")

scenario = st.selectbox("Choose a Scenario", ["Order Coffee", "Introduce Yourself", "Call the Doctor"])

st.markdown(f"### Phrase Example")
if scenario == "Order Coffee":
    st.info('"Hello, I\'d like to order a coffee."')
elif scenario == "Introduce Yourself":
    st.info('"Hi, my name is Sarah."')
else:
    st.info('"Hello, I\'d like to make an appointment."')

if st.button("Listen"):
    st.success("🔊 Simulated playback: TTS playing your chosen phrase...")

if st.button("Speak Now"):
    st.warning("🎙️ Simulated recording... (In a real app, this would use Whisper AI)")

if st.button("Analyze My Speech"):
    st.success("✅ Good job! Your phrase matched well. AI Feedback: Great clarity!")

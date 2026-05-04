import streamlit as st

st.set_page_config(
    page_title="Audio Input Test",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Audio Input Test")
st.write("Click the microphone button below, speak something, then hit stop.")

audio = st.audio_input("Speak something")

if audio is not None:
    st.success("✅ Audio captured! Playing it back below:")
    st.audio(audio)

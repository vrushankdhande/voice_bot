import streamlit as st
from audio_recorder_streamlit import audio_recorder
from gtts import gTTS
import tempfile
from google import genai
from google.genai import types

st.title("🎤 Voice Bot (Stable Version)")

# Record audio from browser
audio_bytes = audio_recorder()

if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # --- Dummy Processing (replace with Gemini later) ---
    response_text = "Hello, I heard you clearly!"

    # Convert to speech
    tts = gTTS(response_text)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)

    st.success(f"Response: {response_text}")

    # Auto play response
    st.audio(temp_file.name)

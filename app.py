import streamlit as st
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase
import numpy as np
from gtts import gTTS
import tempfile

st.title("🎤 Voice Bot (Streamlit Cloud Ready)")

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_data = []

    def recv(self, frame):
        audio = frame.to_ndarray()
        self.audio_data.append(audio)
        return frame

ctx = webrtc_streamer(
    key="speech",
    audio_processor_factory=AudioProcessor,
    media_stream_constraints={"audio": True, "video": False},
)

if st.button("🧠 Process Voice"):
    if ctx.audio_processor:
        audio_chunks = ctx.audio_processor.audio_data

        if audio_chunks:
            audio_np = np.concatenate(audio_chunks, axis=0)

            # Dummy response (replace with Gemini)
            response_text = "Hello, I heard you!"

            # Convert to speech
            tts = gTTS(response_text)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)

            st.audio(temp_file.name)
        else:
            st.warning("No audio captured")

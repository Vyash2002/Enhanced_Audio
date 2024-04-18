import streamlit as st
from st_audiorec import st_audiorec
import base64
import os

def main():
    st.title("Enhanced Audio Recorder")

    # Record audio
    st.write("Click the button below to start recording:")
    audio_data = st_audiorec()

    # Display the recorded audio
    if audio_data:
        st.audio(audio_data, format='audio/wav')

        # Save audio file
        save_file(audio_data)

def save_file(audio_data):
    # Save audio to a file
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_data)

    # Provide a download link for the audio file
    with open("recorded_audio.wav", "rb") as f:
        audio_bytes = f.read()
        audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
        audio_href = f'<a href="data:audio/wav;base64,{audio_b64}" download="recorded_audio.wav">Download Audio</a>'
        st.markdown(audio_href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

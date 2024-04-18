import streamlit as st
from st_audiorec import st_audiorec

def main():
    st.title("Audio Recorder")

    st.write("Click the button below to start recording:")

    # Call the st_audiorec function to record audio
    audio_data = st_audiorec()

    # Display the recorded audio
    if audio_data:
        st.audio(audio_data, format='audio/wav')

if __name__ == "__main__":
    main()

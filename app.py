import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text
import tempfile

st.set_page_config(page_title="AI Lecture Summarizer")

st.title("🎓 AI Lecture Summarizer")
st.write("Upload a lecture audio file to get an AI-generated summary.")

audio_file = st.file_uploader(
    "Upload Lecture Audio",
    type=["mp3", "wav"]
)

if audio_file is not None:
    st.audio(audio_file)
    st.success("Audio uploaded successfully!")

    if st.button("Generate Summary"):
        with st.spinner("Transcribing and summarizing..."):
            # Reset file pointer
            audio_file.seek(0)

            # Save temp audio file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_audio.write(audio_file.read())
                temp_audio_path = temp_audio.name

            # Step 1: Speech to Text
            text = transcribe_audio(temp_audio_path)

            # Step 2: Text to Summary
            summary = summarize_text(text)

        st.subheader("📝 Lecture Summary")
        st.write(summary)

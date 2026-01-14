import os
import whisper

# Explicitly set ffmpeg path for Streamlit Cloud
os.environ["PATH"] += os.pathsep + "/usr/bin"

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Takes an audio file path and returns transcribed text
    """
    result = model.transcribe(audio_path)
    return result["text"]

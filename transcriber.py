import whisper
import os

# Explicitly tell Whisper where ffmpeg is
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Takes an audio file path
    Returns transcribed text
    """
    result = model.transcribe(audio_path)
    return result["text"]

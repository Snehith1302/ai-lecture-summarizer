🎓 AI Lecture Summarizer

An audio-based AI application that converts lecture recordings into concise, structured summaries using speech recognition and transformer-based NLP.

This project demonstrates an end-to-end AI pipeline:
Audio → Speech-to-Text → NLP Summarization → Readable Notes

✨ Key Highlights

🎧 Accepts lecture audio files (MP3 / WAV)

🗣️ Converts speech to text using OpenAI Whisper

🧠 Generates summaries using Transformer NLP models (BART)

🖥️ Simple and intuitive Streamlit interface

🧩 Modular and clean codebase

⚙️ Designed with real-world system constraints in mind

🧠 System Architecture
Lecture Audio
      ↓
Speech-to-Text (Whisper)
      ↓
Text Processing
      ↓
Transformer-based Summarization (BART)
      ↓
Concise Lecture Summary


🛠️ Tech Stack

| Category       | Technology                       |
| -------------- | -------------------------------- |
| Language       | Python                           |
| UI             | Streamlit                        |
| Speech-to-Text | OpenAI Whisper                   |
| NLP            | Hugging Face Transformers (BART) |
| ML Framework   | PyTorch                          |


📂 Project Structure
ai-lecture-summarizer/
├── app.py              # Streamlit UI
├── transcriber.py      # Audio → Text (Whisper)
├── summarizer.py       # Text → Summary (BART)
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── .gitignore

▶️ How to Run Locally

⚠️ This project is intended to be run locally due to audio processing dependencies.

1️⃣ Clone the repository
git clone https://github.com/Snehith1302/ai-lecture-summarizer.git
cd ai-lecture-summarizer

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
streamlit run app.py

📸 Demo (Local Execution)
<img width="1919" height="1005" alt="Screenshot 2026-01-14 232426" src="https://github.com/user-attachments/assets/25e10200-fb7d-4477-a3d7-18ab8ec2409b" />

⚠️ Deployment Note

This application is designed for local execution.

Speech-to-text functionality relies on Whisper, which depends on FFmpeg and system-level audio processing.
Due to limitations in managed cloud platforms, the full audio pipeline is not deployed online.

This design decision ensures:

Stability

Accurate transcription

Reproducibility of results

🎯 Use Cases

📚 Students summarizing recorded lectures

📝 Automatic note generation

🎧 Audio-based content analysis

🧠 Learning-focused AI applications

🚀 Future Enhancements

Cloud-based speech-to-text APIs

Speaker diarization

Timestamped summaries

PDF / DOC export

Multi-language support

👤 Author

Anuka Snehith Reddy
B.Tech – Computer Science and Engineering
AI & ML Enthusiast


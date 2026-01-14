# AI Lecture Summarizer 🎓

An AI-powered web application that converts lecture audio into clear, structured text summaries.

---

## 🚀 Features
- Upload lecture audio files (MP3 / WAV)
- Convert speech to text using Whisper
- Generate concise summaries using Transformer-based NLP
- Simple and interactive Streamlit web interface

---

## 🛠️ Tech Stack
- Python
- Streamlit
- OpenAI Whisper (Speech-to-Text)
- Hugging Face Transformers (BART Large CNN)

---

## 📂 Project Structure
ai-lecture-summarizer/
├── app.py
├── transcriber.py
├── summarizer.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/ai-lecture-summarizer.git
Navigate into the project:

bash
Copy code
cd ai-lecture-summarizer
Create and activate virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
streamlit run app.py
🌐 Deployment
This application can be deployed using Streamlit Cloud directly from the GitHub repository.

🎯 Use Case
Helps students automatically generate notes from recorded lectures, improving learning efficiency and revision.


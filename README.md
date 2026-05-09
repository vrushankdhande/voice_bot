# Voice Bot (Stable Version) 🎤🤖

A simple **Voice Bot Web App** built using **Streamlit** that records audio from the browser, processes the input, and responds back with synthesized speech using **Google Text-to-Speech (gTTS)**.

---

# Features 🚀

- Record voice directly from the browser
- Play recorded audio instantly
- Generate AI/text response
- Convert text response into speech
- Auto-play generated response audio
- Lightweight and beginner-friendly project

---

# Tech Stack 🛠️

- Python
- Streamlit
- audio-recorder-streamlit
- gTTS (Google Text-to-Speech)
- Google Gemini SDK (Ready for future AI integration)

---

# Project Structure 📂

```bash
voice-bot/
│
├── voice_bot.py
├── requirements.txt
└── README.md
```

---

# Installation ⚙️

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/voice-bot.git
cd voice-bot
```

---

## 2. Create Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit
pip install audio-recorder-streamlit
pip install gtts
pip install google-genai
```

---

# Run the Application ▶️

```bash
streamlit run voice_bot.py
```

The app will open automatically in your browser.

---

# Future Improvements 🔥

- Add Speech-to-Text using Gemini API
- Real-time AI conversation
- Multiple voice options
- Chat history support
- Deploy on Streamlit Cloud
- Add multilingual support

---

# Requirements 📦

Example `requirements.txt`

```txt
streamlit
audio-recorder-streamlit
gtts
google-genai
```

---

# Author 👨‍💻

**Vrushank Dhande**

- Python Developer
- Data Science & AI Enthusiast

---

# License 📄

This project is open-source and available under the MIT License.

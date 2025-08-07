# Intelligent-Excusegen-AI
ExcuseGen – AI-powered excuse generator with voice and visual proof  A web app built using Flask that generates smart, believable excuses using Cohere LLM, gTTS for audio, and Stable Diffusion for image proof. Includes dark/light mode, history tracking, and multi-language support.

# 🤖 ExcuseGen – AI-Powered Excuse Generator

ExcuseGen is a web-based application that intelligently generates realistic excuses based on user input. It combines cutting-edge AI technologies to provide not only context-aware text responses, but also speech output and visual proof to support the excuse.

---

## 🔍 Overview

This project leverages:

- **Cohere's LLM** for generating natural language excuses
- **Google Text-to-Speech (gTTS)** for audio voiceovers
- **Stable Diffusion** for WhatsApp-style emergency images
- **Flask** for backend server routing
- **HTML/CSS/JS** for a clean and responsive UI

---

## 🌟 Features

- 🎯 Generate excuses based on situation, tone, urgency, and language
- 🗣️ Voice playback of the excuse (text-to-speech)
- 🖼️ Emergency image generation with Stable Diffusion
- 🌓 Toggle between light and dark mode
- 🧾 Excuse history tracking for user reference
- 🌐 Supports multiple languages (e.g., English, Tamil)

---

## 🚀 Live Demo

> Will be available soon on [Render](https://render.com).

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/excusegen-ai.git
cd excusegen-ai
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Environment Variables

Create a file named `.env` in the root directory and add your API key:

```env
COHERE_API_KEY=your_cohere_api_key_here
```

### 5. Run the Application

```bash
python main.py
```

Access the app at `http://localhost:10000`.

---

## 💻 Tech Stack

| Technology     | Purpose                         |
|----------------|----------------------------------|
| Flask          | Web framework                    |
| Cohere API     | Excuse text generation (LLM)     |
| gTTS           | Convert text to speech           |
| Stable Diffusion | Image generation (proof)       |
| HTML/CSS/JS    | Frontend UI                      |
| Bootstrap      | Responsive layout and styling    |

---

## 📁 Project Structure

```
excusegen-ai/
│
├── templates/              # HTML templates
├── static/                 # CSS, JS, Images, Audio
│   ├── audio/              # Generated voice files
│   └── images/             # WhatsApp-style proof images
├── main.py                 # Main Flask application
├── text_to_speech.py       # gTTS logic
├── image_generator.py      # Stable Diffusion logic
├── excuse_generator.py     # LLM interface (Cohere)
├── history_manager.py      # Local history tracker
├── requirements.txt        # Required Python packages
├── Procfile                # For deployment on Render
├── .env.example            # API key template
└── README.md               # This file
```

---

## 📌 To-Do / Future Enhancements

- ✅ Add download/export option for history
- ✅ Enable multilingual excuse generation
- 🔜 Persistent database (e.g., SQLite or Firebase)
- 🔜 User authentication and saved accounts
- 🔜 Mobile app version

---

## 📝 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 🙌 Acknowledgments

- [Cohere](https://cohere.com)
- [Google Text-to-Speech](https://pypi.org/project/gTTS/)
- [Stable Diffusion](https://stability.ai/)
- [Render](https://render.com) – for free web hosting

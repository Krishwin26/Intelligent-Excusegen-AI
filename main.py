from flask import Flask, render_template, request
from datetime import datetime
import os
import json
from gtts import gTTS
import cohere
from whisper_transcriber import transcribe_audio
from excuse_ranker import rank_excuse
from auto_scheduler import suggest_next_excuse_time
from image_proof import generate_image_proof
from emergency_generator import create_fake_proof_image
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
UPLOAD_FOLDER = "static/generated"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_excuse(situation, scenario, urgency, tone, language):
    prompt = f"Write a realistic, short and believable excuse in {language}. The scenario is {scenario}, urgency: {urgency}, tone: {tone}. Situation: {situation}."
    response = co.generate(
        model='command-xlarge',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    return response.generations[0].text.strip()

def generate_speech(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    temp_path = os.path.join(UPLOAD_FOLDER, f"excuse_{datetime.now().timestamp()}.mp3")
    tts.save(temp_path)
    return temp_path

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        scenario = request.form["scenario"]
        language = request.form["language"]
        urgency = request.form["urgency"]
        tone = request.form["tone"]
        situation = request.form.get("situation", "")
        audio = request.files.get("audio")

        if not situation and audio:
            audio_path = os.path.join(UPLOAD_FOLDER, f"audio_{datetime.now().timestamp()}.wav")
            audio.save(audio_path)
            situation = transcribe_audio(audio_path)

        

        excuse = generate_excuse(situation, scenario, urgency, tone, language)
        language_map = {
               "English": "en",
               "Hindi": "hi",
               "French": "fr",
               "Spanish": "es",
               "German": "de",
               "Tamil": "ta"
}
        tts_lang = language_map.get(language, "en")
        audio_path = generate_speech(excuse, lang=tts_lang)
        score = rank_excuse(excuse, urgency)
        proof_path = generate_image_proof(excuse)
        next_time = suggest_next_excuse_time()
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%A, %d %B %Y")
        fake_proof_path = create_fake_proof_image(scenario, language, current_time, current_date)

        result = {
            "excuse": excuse,
            "audio": audio_path,
            "proof": proof_path,
            "score": score,
            "next_time": next_time,
            "fake_proof": fake_proof_path
        }

        with open("history.json", "a") as f:
            f.write(json.dumps({ "timestamp": str(datetime.now()), "excuse": excuse }) + "\n")

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
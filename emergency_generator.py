from PIL import Image, ImageDraw, ImageFont
import textwrap
from datetime import datetime

def generate_emergency_message(scenario, language="English"):
    messages = {
        "English": {
            "Health": "Your medical appointment is urgently scheduled.",
            "Family Emergency": "Hey there! Some urgent emergency, gotta dash out.",
            "Travel": "Your flight schedule has been changed unexpectedly.",
            "Weather": "Severe weather warning issued in your area.",
            "Technical Issue": "Unexpected technical failure detected on your device."
        }
    }
    return messages.get(language, messages["English"]).get(scenario, "Unexpected urgent situation occurred.")

def create_fake_proof_image(scenario, language, timestamp="10:01 PM", date="Sunday, 14 July 2025"):
    message_text = generate_emergency_message(scenario, language)

    img = Image.new('RGB', (600, 400), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("arial.ttf", 18)
        font_msg = ImageFont.truetype("arial.ttf", 22)
        font_time = ImageFont.truetype("arial.ttf", 12)
    except:
        font_title = font_msg = font_time = ImageFont.load_default()

    draw.rectangle([(0, 0), (600, 60)], fill=(7, 94, 84))
    date_bubble_w, date_bubble_h = 200, 30
    date_bubble_x = (600 - date_bubble_w) // 2
    draw.rounded_rectangle(
        [(date_bubble_x, 65), (date_bubble_x + date_bubble_w, 65 + date_bubble_h)],
        radius=15, fill=(220, 248, 255)
    )
    draw.text((date_bubble_x + 30, 70), date, fill="black", font=font_time)

    bubble_color = (220, 248, 198)
    bubble_x0, bubble_y0 = 40, 110
    bubble_x1, bubble_y1 = 500, 165
    draw.rounded_rectangle([(bubble_x0, bubble_y0), (bubble_x1, bubble_y1)], radius=15, fill=bubble_color)
    wrapped_text = textwrap.fill(message_text, width=60)
    draw.text((bubble_x0 + 35, bubble_y0 + 20), wrapped_text, fill="black", font=font_msg)
    draw.text((bubble_x1 - 80, bubble_y1 - 25), timestamp, fill="gray", font=font_time)

    proof_path = f"static/generated/whatsapp_proof_{hash(message_text) % 10000}.png"
    img.save(proof_path)
    return proof_path
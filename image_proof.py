import torch
from diffusers import StableDiffusionPipeline
import os
from dotenv import load_dotenv

load_dotenv()

model_id = "runwayml/stable-diffusion-v1-5"
token = os.getenv("HUGGINGFACE_TOKEN")

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    use_auth_token=token
)

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

def generate_image_proof(excuse_text):
    prompt = f"realistic document photo to justify excuse: {excuse_text}"
    image = pipe(prompt, num_inference_steps=25).images[0]
    path = f"static/generated/proof_sd_{hash(excuse_text) % 10000}.png"
    image.save(path)
    return path

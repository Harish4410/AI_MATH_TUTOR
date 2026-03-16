import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")

def image_to_equation(image):

    prompt = """
Extract the algebra equation from the image.

Rules:
- Return ONLY the equation
- Convert implicit multiplication (2x → 2*x)
- Use standard math notation

Example output:
2*x + 5 = 15
"""

    response = model.generate_content([prompt, image])

    eq = response.text.strip()

    eq = eq.replace(" ", "")

    return eq
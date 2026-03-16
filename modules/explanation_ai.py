import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_steps(equation):

    prompt = f"""
Explain step-by-step how to solve the algebra equation:

{equation}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        # if quota exceeded, wait and retry once
        if "429" in str(e):

            time.sleep(60)

            response = model.generate_content(prompt)
            return response.text

        return "AI explanation unavailable due to API quota limits."
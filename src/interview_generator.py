import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_questions(prompt):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    cleaned = response.text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

    return json.loads(cleaned)
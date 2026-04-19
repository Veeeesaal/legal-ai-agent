import os
from groq import Groq
from dotenv import load_dotenv
from config import FAST_MODEL

load_dotenv()

class GroqLLM:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=FAST_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
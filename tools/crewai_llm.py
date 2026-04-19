from crewai import LLM
import os
from dotenv import load_dotenv
from config import FAST_MODEL

load_dotenv()

groq_llm = LLM(
    model=FAST_MODEL,
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
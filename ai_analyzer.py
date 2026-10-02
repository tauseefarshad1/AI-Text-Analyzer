from google import genai
from google.genai import errors
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

def summarize(text):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"Summarize the following text in a concise manner:\n\n{text}",
    )
    
    return response.text

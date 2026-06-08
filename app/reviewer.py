from google import genai
import os
import time
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def review_code(filename: str, code: str) -> dict:
    prompt = f"""
You are an expert Python code reviewer.
Review the following Python file named '{filename}' and provide structured feedback.

Return your review in this exact format:

SEVERITY: (Critical / Warning / Suggestion)
ISSUES:
- issue 1
- issue 2
IMPROVEMENTS:
- improvement 1
- improvement 2
SCORE: (a number from 1 to 10)
SUMMARY: (2-3 sentences overall summary)

Code to review:
{code}
"""
    time.sleep(2)
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return {
            "filename": filename,
            "review": response.text
        }
    except Exception as e:
        return {
            "filename": filename,
            "review": f"Error during review: {str(e)}"
        }
    
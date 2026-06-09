import os
import time
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    time.sleep(1)
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {
            "filename": filename,
            "review": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "filename": filename,
            "review": f"Error during review: {str(e)}"
        }
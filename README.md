# AI Code Review Bot

An AI-powered backend tool that automatically reviews Python code from any public GitHub repository using Google Gemini API.

## What it does

- Accepts a public GitHub repository URL
- Fetches Python files from the repository
- Sends each file to Gemini AI for review
- Returns structured feedback with severity level, issues, improvements, and a score

## Tech Stack

- Python 3.11
- FastAPI
- Google Gemini API
- Requests
- Uvicorn

## Project Structure

```
ai-code-review-bot/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── reviewer.py
│   └── github_fetcher.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository
```
git clone https://github.com/Atharva9988/ai-code-review-bot.git
cd ai-code-review-bot
```

2. Create virtual environment
```
py -3.11 -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Create a `.env` file in the root folder
```
GEMINI_API_KEY=your_gemini_api_key_here
```

5. Run the server
```
uvicorn app.main:app --reload
```

6. Open your browser and go to
```
http://localhost:8000/docs
```

## API Usage

### POST /review

Send a public GitHub repo URL and get back AI-generated code reviews.

Request body:
```json
{
  "repo_url": "https://github.com/username/repository"
}
```

Response:
```json
{
  "repo": "https://github.com/username/repository",
  "total_files_reviewed": 3,
  "reviews": [
    {
      "filename": "main.py",
      "review": "SEVERITY: Warning\nISSUES:\n- Missing error handling\nIMPROVEMENTS:\n- Add try/except blocks\nSCORE: 6\nSUMMARY: ..."
    }
  ]
}
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| GEMINI_API_KEY | Your Google Gemini API key from aistudio.google.com |

## Author

Atharva9988
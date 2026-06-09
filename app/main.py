from fastapi import FastAPI
from pydantic import BaseModel
from app.github_fetcher import fetch_github_code
from app.reviewer import review_code

app = FastAPI(title="AI Code Review Bot")

class RepoRequest(BaseModel):
    repo_url: str

@app.get("/")
def root():
    return {"message": "AI Code Review Bot is running"}

@app.post("/review")
def review_repo(request: RepoRequest):
    code_files = fetch_github_code(request.repo_url)

    if "error" in code_files:
        return {"error": code_files["error"]}

    reviews = []
    for filename, code in code_files.items():
        result = review_code(filename, code)
        reviews.append(result)

    return {
        "repo": request.repo_url,
        "total_files_reviewed": len(reviews),
        "reviews": reviews
    }
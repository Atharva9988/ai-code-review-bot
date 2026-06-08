import requests

def fetch_files_from_url(api_url: str, headers: dict, code_files: dict, max_files: int = 5):
    if len(code_files) >= max_files:
        return

    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        return

    files = response.json()

    for file in files:
        if len(code_files) >= max_files:
            break
        if file["type"] == "file" and file["name"].endswith(".py"):
            file_response = requests.get(file["download_url"])
            code_files[file["name"]] = file_response.text
        elif file["type"] == "dir":
            fetch_files_from_url(file["url"], headers, code_files, max_files)

def fetch_github_code(repo_url: str) -> dict:
    try:
        parts = repo_url.rstrip("/").split("/")
        owner = parts[-2]
        repo = parts[-1]

        api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"
        headers = {"Accept": "application/vnd.github.v3+json"}

        code_files = {}
        fetch_files_from_url(api_url, headers, code_files, max_files=5)

        if not code_files:
            return {"error": "No Python files found in this repo."}

        return code_files

    except Exception as e:
        return {"error": str(e)}
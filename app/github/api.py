import requests
from app.config import GITHUB_TOKEN

def get_pr_diff(owner, repo, pr_number):
  url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
  headers = {
    "Authorization" : f"Bearer {GITHUB_TOKEN}",
    "Accept" : "application/vnd.github.v3.diff"
  }
  response = requests.get(url, headers=headers)
  if response.status_code != 200:
    return None
  else:
    return response.text
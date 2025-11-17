from fastapi import FastAPI
from app.github.api import get_pr_diff
from app.github.parser import parse_diff
from app.services.orchestrator import run_agents
import sys

print("RUNNING WITH PYTHON:", sys.executable)

def app():
    app = FastAPI()


    @app.get("/parse/{owner}/{repo}/{pr}")
    def fetch_diff(owner: str, repo : str, pr : int):
        diff = get_pr_diff(owner, repo, pr)
        if not diff:
            return {"error": "failed to fetch diff", "hint": "check GITHUB_TOKEN and permissions"}
        try:
            parsed = parse_diff(diff)
        except Exception as e:
            return {"error": "parser error", "detail": str(e)[:1000]}
        return {"files_count": len(parsed), "sample": parsed[:3]}

    @app.get("/review/{owner}/{repo}/{pr}")
    def review_pr(owner : str, repo : str, pr : int):
        diff = get_pr_diff(owner, repo, pr)

        if not diff:
            return {
                "error": "Failed to fetch PR diff",
                "hint": "The PR may not exist, the repo name may be wrong, or your token may lack permissions."
            }
        
        parsed = parse_diff(diff)
        review = run_agents(parsed)
        return review
    
    return app
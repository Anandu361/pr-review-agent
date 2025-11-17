
# Automated Pull Request Review Agent

A FastAPI-based multi-agent code review system that analyzes GitHub Pull Request diffs and generates structured review comments using Groq LLMs.


## Overview

This system performs automated code reviews by analyzing the actual diff of a GitHub Pull Request.
It extracts modified lines, runs them through a multi-agent review pipeline, and produces actionable feedback—similar to a real human reviewer.




## Features

- Fetches GitHub PR diffs dynamically

- Custom unified diff parser

- 4 specialized review agents:

  - Logic Analysis Agent

  - Performance Agent

  - Security Agent

  - Style & Readability Agent

- Multi-agent orchestration system

- LLM-powered review generation using Groq API

- Clean JSON review output, ready for API consumption or UI display

- Built completely with Python + FastAPI


## Components

- GitHub Fetcher: Retrieves raw .diff for any PR using GitHub REST API.
- Diff Parser: Converts unified diff into structured objects:
```json
{
  "file_path": "...",
  "changes": [
    {"line": 10, "type": "added", "code": "print('test')"},
    {"line": 10, "type": "removed", "code": "print('old')"}
  ]
}
```
- Agents: Each agent is an independent module with its own prompt.
- Orchestrator: Runs all agents and merges feedback.
- LLM Service: Uses Groq (Llama 3.1 models) for generating review comments.


## Installation

1️⃣ Clone the repository

```bash
  git clone https://github.com/Anandu361/pr-review-agent
  cd pr-review-agent
```
2️⃣ Create a virtual environment

```bash
  python -m venv myvenv
  source myvenv/bin/activate       # Mac/Linux
  myvenv\Scripts\activate          # Windows
```
3️⃣ Install dependencies

```bash
  pip install -r requirements.txt
```
4️⃣ Create .env
```bash
  GITHUB_TOKEN=your_github_token
  GROQ_API_KEY=your_groq_key
```
5️⃣ Run the server
```bash
  uvicorn app.main:app --reload
```

## API Endpoints

Get the parsed diff
```bash
  GET /parse/{owner}/{repo}/{pr}
```
Run full PR review
```bash
  GET /review/{owner}/{repo}/{pr}
```
Example
```bash
  /review/facebook/react/27590
```



    
## Example Output

```json
[
  {
    "file": "src/index.js",
    "logic": [
      {"line": 12, "comment": "Potential logical error..."}
    ],
    "performance": [
      {"line": 27, "comment": "Loop can be optimized..."}
    ],
    "security": [
      {"line": 33, "comment": "Unsafe eval usage detected..."}
    ],
    "style": [
      {"line": 8, "comment": "Follow PEP8 naming convention."}
    ]
  }
]
```


## Tech Stack

- Python 3

- FastAPI

- Groq LLM (Llama 3.1 models)

- Requests

- Custom diff parsing

- Multi-agent orchestration




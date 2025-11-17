from groq import Groq
import json
import os
from dotenv import load_dotenv

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def llm_run(prompt):
    res = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

def safe_parse(text: str):
  try:
    return json.loads(text)
  
  except:
    return [{"line": None, "comment": text}]
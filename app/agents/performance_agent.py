from app.services.llm_service import llm_run, safe_parse

def performance_agent(file_data: dict) -> list:
  prompt = f"""
    You are a performance code review agent...
    File: {file_data['file_path']}
    Changes: {file_data['changes']}
    Respond STRICTLY in JSON:
    [
      {{"line": <number>, "comment": "<message>"}}
    ]
  """

  response = llm_run(prompt)

  return safe_parse(response)
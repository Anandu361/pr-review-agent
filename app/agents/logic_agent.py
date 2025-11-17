from app.services.llm_service import llm_run, safe_parse

def logic_agent(file_data: dict) -> list:
  prompt = f"""
    You are  code review assistant. Analyze the following code changes for logical issues.
    File: {file_data['file_path']}
    Changes: {file_data['changes']}
    Respond with a list of comments in this format:
    [
      {{
        "line": <line_number>,
        "comment": "<message>"
      }}]
  """
  response = llm_run(prompt)

  return safe_parse(response)

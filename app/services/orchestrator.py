from app.agents.logic_agent import logic_agent
from app.agents.performance_agent import performance_agent
from app.agents.security_agent import security_agent
from app.agents.style_agent import style_agent

def run_agents(parsed_files: list) -> dict:
  review_comments = []

  for file in parsed_files:
    logic_comments = logic_agent(file)
    performance_comments = performance_agent(file)
    security_comments = security_agent(file)
    style_comments = style_agent(file)

    review_comments.append({
      "file" : file["file_path"],
      "logic" : logic_comments,
      "performance" : performance_comments,
      "security" : security_comments,
      "style" : style_comments,
    })

  return review_comments
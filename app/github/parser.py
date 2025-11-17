def parse_diff(diff_text : str):
  lines = diff_text.split("\n")

  parsed_files = []
  current_file = None
  new_line = 0
  old_line = 0

  for line in lines:
    if line.startswith("diff --git"):
      if current_file is not None:
        parsed_files.append(current_file)
      parts = line.split()
      new_path = parts[3]
      file_path = new_path[2:]

      current_file = {
        "file_path" : file_path,
        "changes" : []
      }
      continue

    if line.startswith("@@"):
      header = line.split("@@")[1].strip()
      parts = header.split()
      old_part = parts[0]
      new_part = parts[1]

      old_line = int(old_part[1:].split(",")[0] or 0)
      new_line = int(new_part[1:].split(",")[0] or 0)
      continue


    if line.startswith("+++") or line.startswith("---"):
      continue

    if line.startswith("+") and not line.startswith("+++"):
      current_file["changes"].append({
        "line" : new_line,
        "type" :"added",
        "code" : line[1:]
      })
      new_line += 1
      
    
    if line.startswith("-") and not line.startswith("---"):
      current_file["changes"].append({
        "line" : old_line,
        "type" :"removed",
        "code" : line[1:]
      })

      old_line += 1

    if line.startswith(" "):
      new_line +=1
      old_line +=1

    if current_file is None:
      continue

  parsed_files.append(current_file)
  return parsed_files
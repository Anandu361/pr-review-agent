import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))


from app.github.parser import parse_diff

with open("tests/sample_diff.txt", "r") as f:
    text = f.read()

result = parse_diff(text)
print(result)

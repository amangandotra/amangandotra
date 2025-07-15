import requests
import re

username = "amangandotra" 
leetcode_api = f"https://leetcode-stats-api.herokuapp.com/{username}"

try:
    response = requests.get(leetcode_api, timeout=10)
    data = response.json()
    rank = data.get("ranking", "N/A")
except Exception as e:
    rank = "Error"

# === Step 2: Random Quote ===
try:
    quote_response = requests.get("https://api.quotable.io/random", timeout=10)
    quote = quote_response.json().get("content", "Stay curious, keep learning.")
except Exception:
    quote = "Stay curious, keep learning."

# === Step 3: Update README.md ===
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r"\{\{LEETCODE_RANK\}\}", str(rank), content)
content = re.sub(r"\{\{QUOTE\}\}", quote, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

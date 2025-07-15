import requests
import re

username = "amangandotra" 
url = f"https://leetcode-api.jacoblin.cool/{username}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()
    rank = data["data"].get("ranking", "N/A")
except Exception as e:
    rank = "Error"

# === Get Random Quote ===
try:
    quote_response = requests.get("https://api.quotable.io/random", timeout=10)
    quote = quote_response.json().get("content", "Stay curious, keep learning.")
except:
    quote = "Stay curious, keep learning."

# === Update README.md ===
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r"\{\{LEETCODE_RANK\}\}", str(rank), content)
content = re.sub(r"\{\{QUOTE\}\}", quote, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

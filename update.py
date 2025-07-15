import requests
import re

# === Get Random Quote ===
try:
    quote_response = requests.get("https://api.quotable.io/random", timeout=10)
    quote = quote_response.json().get("content", "Stay curious, keep learning.")
except:
    quote = "Stay curious, keep learning."

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r"\{\{QUOTE\}\}", quote, content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

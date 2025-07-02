import requests
import os
from datetime import datetime
from config import api_key

# --------------- API Setup ---------------
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# --------------- Get User Input ---------------
print("\n📝 Enter the text you'd like summarized (Press Enter twice to finish):\n")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

text_to_summarize = "\n".join(lines).strip()

if not text_to_summarize:
    print("⚠️ No text provided. Exiting.")
    exit()

# --------------- Call GPT for Summary ---------------
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You summarize the provided text."},
        {"role": "user", "content": f"Summarize this text:\n{text_to_summarize}"}
    ],
    "max_tokens": 150
}

try:
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    result = response.json()
    summary = result["choices"][0]["message"]["content"].strip()

    print("\n✅ Summary:\n", summary)

except Exception as e:
    print(f"❌ API Error: {e}")
    exit()

# --------------- Save Summary to File ---------------
os.makedirs("summaries", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"summaries/Summary_{timestamp}.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(summary)

print(f"\n📁 Summary saved to '{output_file}'")

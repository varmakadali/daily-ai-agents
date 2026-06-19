import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def build_digest(updates: list) -> str:
    items_text = ""
    for i, item in enumerate(updates[:20], 1):
        items_text += f"{i}. TITLE: {item['title']}\n"
        items_text += f"   SOURCE: {item['source']} | CATEGORY: {item['category']}\n"
        items_text += f"   CONTENT: {item['content'][:300]}\n"
        items_text += f"   URL: {item['url']}\n\n"

    prompt = f"""You are a daily AI news analyst. Here are today's updates:

{items_text}

Create a daily digest with:
1. TOP 5 AI UPDATES (2-line summary each + why it matters)
2. TOP 3 INTERNSHIP/JOB OPPORTUNITIES
3. ONE YouTube Shorts script (60 seconds)
4. ONE LinkedIn post (under 150 words)

Mark urgent items as URGENT. Keep language simple."""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 2000
        }
    )

    data = response.json()
    if "choices" in data:
        return data["choices"][0]["message"]["content"]
    else:
        print("Groq API Error:", data)
        return "Error: Could not generate digest. Check API key."
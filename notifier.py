import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram(message: str):
    # Save to file first
    with open("digest_output.txt", "w", encoding="utf-8") as f:
        f.write(message)
    print("Digest saved to digest_output.txt!")
    
    # Try Telegram
    chunks = [message[i:i+4000] for i in range(0, len(message), 4000)]
    for chunk in chunks:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        try:
            response = requests.post(url, json={
                "chat_id": CHAT_ID,
                "text": chunk
            }, timeout=15)
            print("Telegram sent:", response.status_code)
        except Exception as e:
            print(f"Telegram blocked - but digest is saved in file!")
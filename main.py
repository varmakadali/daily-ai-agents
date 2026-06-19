from searcher import collect_all_updates
from summarizer import build_digest
from notifier import send_telegram

def run():
    print("Step 1: Collecting updates...")
    updates = collect_all_updates()
    print(f"Found {len(updates)} items!")

    print("Step 2: Generating digest...")
    digest = build_digest(updates)
    print("Digest ready!")

    print("Step 3: Sending to Telegram...")
    send_telegram(digest)
    print("Done! Check your Telegram.")

if __name__ == "__main__":
    run()
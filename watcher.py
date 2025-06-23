import requests
import hashlib
import time
import os

INTERVAL = int(os.getenv('WATCH_INTERVAL', '300'))
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
URLS = [url.strip() for url in os.getenv('WATCH_URLS', '').split(',') if url.strip()]

def get_website_hash(url):
    try:
        response = requests.get(url)
        content = response.text
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    except Exception as e:
        print(f"[{url}] Error fetching content: {e}")
        return None

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def monitor():
    hashes = {}

    # Initiale Hashes laden
    for url in URLS:
        h = get_website_hash(url)
        if h:
            hashes[url] = h
            print(f"[{url}] Initial hash stored.")
        else:
            print(f"[{url}] Could not get initial hash.")

    print("⏳ Monitoring started...")
    while True:
        time.sleep(INTERVAL)
        for url in URLS:
            current_hash = get_website_hash(url)
            if current_hash and current_hash != hashes.get(url):
                print(f"[{url}] Change detected!")
                send_telegram_message(f"Content of {url} has changed!")
                hashes[url] = current_hash
            else:
                print(f"[{url}] No change.")

if __name__ == "__main__":
    if not URLS:
        print("⚠️  No valid URLs found in WATCH_URLS.")
    else:
        monitor()
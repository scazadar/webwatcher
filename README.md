# 📘 WebWatcher

## 🔍 WebWatcher – Website Monitoring with Telegram Alerts

**WebWatcher** is a lightweight Docker-based tool for monitoring website content. It regularly checks one or more URLs for content changes and sends Telegram alerts when differences are detected.

---

## 🚀 Features

- Monitor multiple websites with ease
- Change detection using SHA256 hash of HTML content
- Telegram notifications on change
- Fully configurable via environment variables

---

## 📦 Prerequisites

- Docker installed
- Telegram-Bot created via `@BotFather`
- Telegram-Chat-ID (Telegram Chat with Bot or Group)
<details>
<summary>📡 How to Set Up Telegram Notifications for Any Application or Script</summary>

This guide explains how to:

- ✅ Create a Telegram bot
- ➕ Add the bot to a private or group chat
- 📬 Send notifications via Telegram from any app or script

---

## 1. 🤖 Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Type: `/newbot`
3. Follow the steps to set a name and username (username must end in `bot`)
4. Copy the **API token** provided — this is required to send messages

---

## 2. 👤 Get Your Chat ID

To send messages to yourself or a group, you need a **chat ID**.

### For a private chat:
1. Send any message (e.g., "hello") to your bot
2. Visit the following URL (replace `<TOKEN>` with your bot's token):
   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```
3. Look for `"chat":{"id":YOUR_ID,...}` in the JSON response — that's your chat ID

### For a group chat:
1. Create a Telegram group
2. Add your bot to the group
3. Send a message in the group
4. Visit the same URL again and find the group `"chat":{"id":-XXXXXXXXXX,...}`  
   (Note: group IDs are negative numbers)


## 3. 🖼️ Optional: Set a Bot Profile Picture

1. Go back to **@BotFather**
2. Type `/setuserpic`
3. Choose your bot
4. Upload a square image (JPG or PNG)

---

## 4. 🔐 Who Can Receive Messages?

- Your bot **can only send messages to chats** it has been part of
- **Users must start a chat** with the bot or be in a group the bot is added to
- The bot **cannot message random users**

---

## ✅ Done!

You now have:

- 📬 Telegram notifications from any script, app, or automation
- 📢 Group or private alerts

</details>


---

## ⚙️ Environment Variables

| Variable             | Beschreibung                                                                 |
|----------------------|------------------------------------------------------------------------------|
| `WATCH_URLS`         | Kommagetrennte Liste von URLs, z. B. `https://example.com,https://test.org` |
| `WATCH_INTERVAL`     | Intervall in Sekunden zwischen den Checks (Standard: 300)                    |
| `TELEGRAM_TOKEN`     | Bot-Token deines Telegram-Bots                                               |
| `TELEGRAM_CHAT_ID`   | Deine Telegram-Chat-ID (an die die Nachricht gesendet wird)                  |

---

## 🐳 Docker-Build

```bash
docker build -t webwatcher .
```

## 🐳 Docker-Run
```bash
docker run -d \
  --name webwatcher \
  -e WATCH_URLS="https://example.com,https://example.org/page" \
  -e WATCH_INTERVAL=300 \
  -e TELEGRAM_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ \
  -e TELEGRAM_CHAT_ID=123456789 \
  webwatcher
```
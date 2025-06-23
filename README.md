# 📘 WebWatcher

## 🔍 Website-Monitoring mit Telegram-Benachrichtigung (Docker)

Dieses Projekt überwacht eine oder mehrere Webseiten regelmäßig auf Inhaltsänderungen und sendet bei einer Änderung eine Nachricht via Telegram.

---

## 🚀 Features

- Überwachung beliebig vieler Webseiten per URL
- Änderungserkennung über SHA256-Hash des Inhalts
- Telegram-Benachrichtigung bei Änderungen
- Docker-basiert: portabel und leicht einsetzbar

---

## 📦 Voraussetzungen

- Docker installiert
- Telegram-Bot erstellt via `@BotFather`
- Telegram-Chat-ID (von deinem Chat mit dem Bot)

---

## ⚙️ Umgebungsvariablen

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

import time
import requests

# === НАСТРОЙКА ===
TELEGRAM_TOKEN = "7577718414:AAGVY6Cg5Xdfl_8ChLyirHRQWKcLYPKaFns"  # <-- вставь свой токен
CHAT_ID = "756770500"  # <-- вставь свой Telegram user ID (можно получить через @userinfobot)
LOG_FILE = "/var/log/kibana/kibana-server-log.log"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

def follow_log(file_path):
    with open(file_path, "r") as f:
        f.seek(0, 2)  # Перейти в конец файла
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            send_to_telegram(f"📄 Новый лог:\n`{line.strip()}`")

if __name__ == "__main__":
    follow_log(LOG_FILE)

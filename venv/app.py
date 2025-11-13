from flask import Flask, jsonify
import time
import logging

app = Flask(__name__)

# === Налаштування журналювання ===
logging.basicConfig(
    filename='app.log',          # файл для збереження логів
    level=logging.INFO,          # рівень логування (мінімальний)
    format='%(asctime)s [%(levelname)s] %(message)s'  # формат повідомлення
)

# === Глобальні змінні для статусу ===
start_time = time.time()
request_count = 0


@app.before_request
def before_request():
    """Перед кожним запитом збільшуємо лічильник і пишемо лог."""
    global request_count
    request_count += 1
    logging.info(f"Отримано запит №{request_count}")


@app.route("/")
def home():
    logging.info("Запит до '/' — Сервіс працює")
    return "Сервіс працює"


@app.route("/error")
def error():
    """Маршрут, який навмисно викликає помилку."""
    logging.warning("Запит до '/error' — зараз буде помилка!")
    try:
        return 1 / 0   # ZeroDivisionError
    except Exception as e:
        logging.error(f"Помилка у '/error': {e}")
        return "Виникла помилка у застосунку!", 500


@app.route("/status")
def status():
    """Повертає JSON з короткою інформацією про роботу застосунку."""
    uptime = round(time.time() - start_time, 2)
    data = {
        "status": "ok",
        "uptime_seconds": uptime,
        "requests_handled": request_count
    }
    logging.info("Запит до '/status' — повертаємо стан застосунку")
    return jsonify(data)


if __name__ == "__main__":
    logging.info("🚀 Flask-застосунок запускається...")
    app.run(debug=True)
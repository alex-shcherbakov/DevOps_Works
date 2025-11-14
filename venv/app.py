from flask import Flask, jsonify
import time
import logging
import socket

app = Flask(__name__)

# налаштування журналювання
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# параметри для UDP-сервера ===
STATS_SERVER = ("127.0.0.1", 9999)  # IP і порт сервера

# Надсилає коротке повідомлення на UDP-сервер
def send_to_statsd(message: str):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode("utf-8"), STATS_SERVER)
        sock.close()
    except Exception as e:
        logging.error(f"Failed to send message to StatsD: {e}")


# глобальні змінні
start_time = time.time()
request_count = 0


@app.before_request
def before_request():
    global request_count
    request_count += 1
    logging.info(f"Received request №{request_count}")


@app.route("/")
def home():
    logging.info("Request to '/' — Service is running")
    return "The service is working"


@app.route("/error")
def error():
    logging.warning("Request to '/error' — there will be an error!")
    return 1 / 0


@app.route("/status")
def status():
    uptime = round(time.time() - start_time, 2)
    data = {
        "status": "ok",
        "uptime_seconds": uptime,
        "requests_handled": request_count
    }
    logging.info("Request to '/status' — return the application status")
    return jsonify(data)


# глобальний обробник винятків
@app.errorhandler(Exception)
def handle_exception(e):
    #логування будь-якої помилки + надсилання у StatsD.
    logging.exception("An unexpected error occurred in the Flask application.")
    send_to_statsd(f"ERROR: {str(e)}")
    return jsonify({"error": "An internal server error has occurred."}), 500


if __name__ == "__main__":
    logging.info("Flask application starts...")
    app.run(debug=True)

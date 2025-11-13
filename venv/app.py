from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()

request_count = 0


@app.before_request
def before_request():
    global request_count
    request_count += 1


@app.route("/")
def home():
    return "Сервіс працює"

# викликає помилку
@app.route("/error")
def error():
    return 1 / 0  # ZeroDivisionError

# повертає JSON
@app.route("/status")
def status():
    uptime = round(time.time() - start_time, 2)
    data = {
        "status": "ok",
        "uptime_seconds": uptime,
        "requests_handled": request_count
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
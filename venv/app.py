from http.cookiejar import debug

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello for QA from Flask"

if __name__=="__main__":
    app.run(debug=True)
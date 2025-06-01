# Simple web application using Flask framework
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello, Rudy Lee, feel free to check! </p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
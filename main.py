from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "New version deployed via Cloud Build! v2"


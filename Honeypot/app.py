from flask import Flask, render_template
import json
import os

app = Flask(__name__)

LOG_FILE = os.path.join(os.path.dirname(__file__), "logs.txt")

def read_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    logs.append(json.loads(line))
    return logs[::-1]

@app.route("/")
def dashboard():
    logs = read_logs()
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
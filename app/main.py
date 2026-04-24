from flask import Flask
import os

app = Flask(__name__)
COUNTER_FILE = "/data/counter.txt"

def read_counter():
    if not os.path.exists(COUNTER_FILE):
        return 0
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip())

def write_counter(value):
    os.makedirs(os.path.dirname(COUNTER_FILE), exist_ok=True)
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

@app.route("/")
def hello():
    count = read_counter() + 1
    write_counter(count)
    return f"Hello! You are visitor #{count}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

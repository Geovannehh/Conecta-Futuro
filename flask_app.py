"""Conecta Futuro — orientação para explorar graduações."""
from flask import Flask, send_from_directory
app = Flask(__name__, static_folder="static")
@app.get("/")
def index():
    return send_from_directory("static", "index.html")
@app.get("/health")
def health():
    return {"service": "conecta-futuro", "status": "ok"}
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

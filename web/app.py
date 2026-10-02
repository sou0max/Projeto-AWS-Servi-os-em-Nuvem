import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# IP privado da EC2 do back-end, passado por variável de ambiente
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:25000")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/dados")
def api_dados():
    try:
        r = requests.get(f"{BACKEND_URL}/dados", timeout=5)
        return jsonify(r.json())
    except requests.RequestException as e:
        return jsonify({"erro": str(e)}), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

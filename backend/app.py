from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/dados")
def dados():
    return jsonify({
        "mensagem": "Olá do back-end!",
        "itens": ["Docker", "AWS EC2", "VPC", "Security Groups"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=25000)

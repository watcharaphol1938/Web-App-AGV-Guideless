from flask import jsonify
from backend import create_app

app = create_app()

@app.route("/country", method = ["GET"])
def country():
    return "ok"

@app.route("/amr", mrthod = ["GET"])
def get_amr():
    amr = [{"id" : 1, "name" : "A"}, {"id": 2, "name" : "B"}]
    return jsonify(amr)

if __name__ == "__main__":
    app.run(host = "192.168.100.125", port = "8081")
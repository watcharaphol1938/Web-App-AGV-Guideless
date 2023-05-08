from flask import Flask

# @app.route("/")
def create_app():
    app = Flask(__name__)
    return app
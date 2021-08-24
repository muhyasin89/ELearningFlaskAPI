import json

from flask import Blueprint, Flask, request

app = Flask(__name__)


@app.route("/test")
def test():
    return "Hello, World!"


@app.route("/")
def hello():
    hello_json = {"message": "Hello, World!", "status": "success"}

    return json.dumps(hello_json)


def create_app():
    # create a minimal app

    return app


if __name__ == "__main__":
    create_app()

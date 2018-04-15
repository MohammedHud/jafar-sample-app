import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, SciTech !!</h1>"


@app.route("/env")
def env():
    return "env: {}. <br/> Running on machine: {}.".format(os.environ.get("ENVIRONMENT", "DEVELOPMENT"),
                                                           socket.gethostname())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

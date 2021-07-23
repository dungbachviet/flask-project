from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import session, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!!"


if __name__ == "__main__":
    app.run(debug=True)

"Flask Up to Speed b2b"
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    "Flask basic render"
    return render_template("card.html")


if __name__ == "__main__":
    app.run(debug=True)

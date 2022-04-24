import websockets
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

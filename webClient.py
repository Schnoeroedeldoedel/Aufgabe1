from flask import Flask, render_template, url_for, request
from client import ClientConnection

app = Flask(__name__)
client = ClientConnection("localhost", 6765)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        client.req_login(username, password)

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

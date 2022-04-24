import asyncio

from flask import Flask, render_template, url_for, request
import client2
from threading import Thread

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # sende hier an den server
        client2.check_login(username, password)
        client2.get_schema()
    return render_template("login.html")


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client2.communicate())
    loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    app.run(debug=True)

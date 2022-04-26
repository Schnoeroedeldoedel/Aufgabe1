import asyncio
import json

from flask import Flask, render_template, url_for, request, redirect

import client
from threading import Thread

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # sende hier an den server
        check = client.check_login(username, password)
        schema = client.get_schema()
        print(check)
        print(schema)
        return redirect(url_for("courses"))
    else:
        return render_template("login.html")


@app.route("/all_courses", methods=["POST", "GET"])
def courses():
    all_courses = client.get_all_courses()
    print(all_courses)
    dic = dict(json.loads(all_courses))

    return render_template("courses.html", content=dic)


@app.route("/all_courses/<course_id>")
def course_info(course_id):
    info = client.get_course_info(course_id)
    return render_template("course-info.html", course = info)


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client.communicate())
    loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    app.run(debug=True)

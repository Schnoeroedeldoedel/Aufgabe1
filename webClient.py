import asyncio
import json

import flask_login
import xmlschema
import xml.etree.ElementTree as ET
from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, logout_user
import client
from threading import Thread

app = Flask(__name__)
app.secret_key = 'super secret string'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    user = User()
    user.id = username
    return user


@login_manager.request_loader
def request_loader(req):
    username = req.form.get('username')
    password = req.form.get('password')

    if username is None or password is None:
        return
    if not client.check_login(username, password):
        return

    user = User()
    user.id = username
    return user


@app.route("/", methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if client.check_login(username, password):
            user = User()
            user.id = username
            flask_login.login_user(user)
            return redirect(url_for("courses"))
        return render_template("login.html", error="Falsche Login Daten")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/booked_courses/<username>")
@flask_login.login_required
def booked_courses(username):
    booked = client.get_booked_courses(username)
    return render_template("courses.html", content=booked)


@app.route("/book_course/<username><id>")
@flask_login.login_required
def book_course(course_id, username):
    return redirect(url_for("courses.html", course_id=course_id))


@app.route("/all_courses", methods=["POST", "GET"])
@flask_login.login_required
def courses():
    all_courses = client.get_all_courses()
    print(all_courses)
    dic = dict(json.loads(all_courses))

    return render_template("courses.html", content=dic)


def xml_to_html(xml):
    ret = ""
    schema = client.get_schema()
    # xsd = xmlschema.XMLSchema(schema)
    # xsd.is_valid(xml)
    root = ET.fromstring(xml)
    return recurse_html(root, 0)


def recurse_html(element, indent):
    ret = ""
    for child in element:
        ret += f"<div style='display: flex'>\n" \
               f"<div style ='width: {5 * indent}%'></div>" \
               f"<span style='color:red; width: {40 - 5 * indent}%;'>{child.tag.capitalize()} : </span>"

        if child.text is not None:
            ret += f"<span style='width: 60%;'>{child.text} </span>"
        ret += f"</div>"
        ret += recurse_html(child, indent + 1)

    return ret


@app.route("/all_courses/<course_id>")
def course_info(course_id):
    xml = client.get_course_info(course_id)
    html = xml_to_html(xml)
    return render_template("course-info.html", id=course_id, course=html)


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client.communicate())
    loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()

    app.run(debug=True)

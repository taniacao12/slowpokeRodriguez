import os, csv, time, sqlite3, json
from urllib.request import Request, urlopen

from flask import Flask, render_template, request,session,url_for,redirect,flash

from util import db

app = Flask(__name__)

app.secret_key = os.urandom(32) #key for session


user = "a"
passw = "b"

@app.route("/")
def home():
    if "logged_in" in session:
        return render_template("home.html", user = session["logged_in"])
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in")
    return redirect(url_for("home"))

@app.route("/auth")
def auth():
    if user == request.args["username"] and passw == request.args["password"]:
        session["logged_in"] = request.args["username"]
        return redirect(url_for("home"))

    flash("Username or password is incorrect")
    return render_template("login.html")


    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()

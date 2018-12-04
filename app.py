import os, csv, time, sqlite3, json
from urllib.request import Request, urlopen

from flask import Flask, render_template, request,session,url_for,redirect,flash

from util import db
from util import api

app = Flask(__name__)

app.secret_key = os.urandom(32) #key for session

@app.route("/")
def home():
    if "logged_in" in session:
        return render_template("home.html", user = session["logged_in"], logged_in=True, recipes=api.search())
    return render_template("home.html", logged_in=False, recipes=api.search())

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/adduser")
def adduser():
    user = request.args["username"].strip()
    password = request.args["password"]
    passwordc = request.args["confirm-password"]

    if(not user or not password or not passwordc):
        flash("Please fill in all fields")
        return redirect(url_for("register"))

    if(db.check_user(user)):
        flash("User already exists")
        return redirect(url_for("register"))

    if(password != passwordc):
        flash("Passwords don't match")
        return redirect(url_for("register"))

    db.add_user(user, password)
    session["logged_in"] = request.args["username"]
    return redirect(url_for("home"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in")
    return redirect(url_for("home"))

#User personalization screen after registered
@app.route("/profile")
def profile_personalize():
    return redirect(url_for("home"))

@app.route("/auth")
def auth():
    if db.auth_user(request.args["username"], request.args["password"]):
        session["logged_in"] = request.args["username"]
        return redirect(url_for("home"))
    else:
        flash("username or password is incorrect")
        return redirect(url_for("login"))

#@app.route("/search", methods = ["POST"])
#ef searching():
#    return render_template("search.html")

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

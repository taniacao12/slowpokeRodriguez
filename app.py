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
        return render_template("home.html", user = session["logged_in"], logged_in=True, recipes=api.search("chicken"))
    return render_template("home.html", logged_in=False, recipes=api.get_recipes("chicken"))

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
    return redirect(url_for("profile"))

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in")
    return redirect(url_for("home"))

#User personalization screen after registered
@app.route("/profile")
def profile():
    preferences = db.get_preference(session["logged_in"])
    # print("app route preferencesd!!!!!: : : : ::")
    print(preferences)
    return render_template("profile.html", user=session["logged_in"], preferences=preferences, logged_in=True)

@app.route("/auth")
def auth():
    if db.auth_user(request.args["username"], request.args["password"]):
        session["logged_in"] = request.args["username"]
        return redirect(url_for("home"))
    else:
        flash("username or password is incorrect")
        return redirect(url_for("login"))

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/dbadd")
def added():
    db.add_recipe(session["logged_in"], request.args["title"],request.args["ingredients"],request.args["instructions"],request.args["link"])
    return redirect(url_for("userentries"))

@app.route("/userentries")
def userentries():
    if "logged_in" in session:
        return render_template("userfood.html", user = session["logged_in"], logged_in=True, recipes= db.user_recipes())
    return render_template("userfood.html", logged_in=False, recipes= db.user_recipes())

@app.route("/updatepreferences")
def update_preferences():
    preferences = request.args["preference"].strip()
    if not preferences:
        db.update("none", session['logged_in'])
    else:
        db.update(preferences, session['logged_in'])
    return redirect(url_for("profile"))

if __name__ == "__main__":
    app.debug = True
    app.run()

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
        return render_template("home.html", user = session["logged_in"], logged_in=True, recipes=api.get_recipes(session["logged_in"]))
    return render_template("home.html", logged_in=False, recipes=api.get_recipes(""))

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
def dbadd():
    user = session["logged_in"].strip()
    recipe_name = request.args["title"].strip()
    ingredients = request.args["ingredients"].strip()
    instructions = request.args["instructions"].strip()
    image = request.args["link"]
    if not user or not recipe_name or not ingredients or not instructions:
        flash("Please fill in all fields")
        return redirect(url_for("addrecipe"))
    db.add_recipe(user, recipe_name, ingredients, instructions, image)
    return redirect(url_for("userentries"))

@app.route("/userentries")
def userentries():
    if "logged_in" in session:
        return render_template("userfood.html", user = session["logged_in"], logged_in=True, recipes= db.user_recipes())
    return render_template("userfood.html", logged_in=False, recipes= db.user_recipes())

@app.route("/updatepreferences")
def update_preferences():
    preferences = request.args["preference"].strip()
    if len(request.args["preference"].split(",")) < 3:
        flash("Enter 3 or more preferences please")
        return redirect(url_for("profile"))

    if not preferences:
        db.update("none", session['logged_in'])
    else:
        flash("Preferences updated")
        db.update(preferences, session['logged_in'])
    return redirect(url_for("profile"))

@app.route("/viewrecipe")
def viewrecipe():
    recipe_id = request.args["recipe-id"]
    recipe = api.find_recipe(recipe_id)
    print("ROUTE STUFFF")
    print(recipe)

    return render_template("viewrecipe.html", name=recipe["name"],
                                              image_url=recipe["image_url"],
                                              source_url=recipe["source_url"],
                                              ingredients=recipe["ingredients"],
                                              servings=recipe["servings"],
                                              rating=recipe["rating"])

@app.route("/removerecipe")
def removerecipe():
    recipe_name = request.args["removing"]
    db.remove_recipe(recipe_name)
    return redirect(url_for("userentries"))


if __name__ == "__main__":
    app.debug = True
    app.run()

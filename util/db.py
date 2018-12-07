import sqlite3

DB_FILE="discobandit.db" # db used for this project. delete file if you want to remove all data/login info.


def create_tables():
    db = sqlite3.connect(DB_FILE) # Open if file exists, otherwise create
    c = db.cursor()

    c.execute("CREATE TABLE if not exists user_info(username TEXT PRIMARY KEY, password TEXT, preferences TEXT)")
    c.execute("CREATE TABLE if not exists recipes(user TEXT, title TEXT, ingredients TEXT, instructions TEXT, images TEXT)")

    db.commit()

    db.close()

def add_user(username, password):
    ''' insert credentials for newly registered user into database '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO user_info VALUES(?, ?, {})".format("'none'"), (username, password))

    db.commit() #save changes
    db.close() #close database

def check_user(username):
    ''' check if a username has already been taken when registering '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for entry in c.execute("SELECT user_info.username FROM user_info"):
        if(entry[0] == username):
            db.close()
            return True

    db.close()
    return False

def auth_user(username, password):
    ''' authenticate a user attempting to log in '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for entry in c.execute("SELECT user_info.username, user_info.password FROM user_info"):
        if(entry[0] == username and entry[1] == password):
            db.close()
            return True

    db.close()
    return False

def add_recipe(username, name, ingred, instruct, pics):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("INSERT INTO recipes VALUES(?,?,?,?,?)", (username, name, ingred, instruct, pics))
    db.commit()
    db.close()
    return True

def user_recipes():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    recipes = {}
    i = 0
    for num in c.execute("SELECT * FROM recipes"):
        recipes[i] = [
            num[0],
            num[1],
            num[2],
            num[3],
            num[4],
        ]
        i += 1
    db.close()
    # print(recipes)
    return recipes

def get_recipe_info(user, title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    recipe = []
    for i in c.execute("select * from recipes where user={} and title={}".format("'" + user + "'", "'" + title + "'")):
        recipe.append(i[0])
        recipe.append(i[1])
        recipe.append(i[2])
        recipe.append(i[3])
        recipe.append(i[4])

    return recipe
    db.close()

def get_preference(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    preference = []
    for i in c.execute("select preferences from user_info where username='" + username + "'"):
        preference = i[0].split(",")

    return preference
    db.close()

def update(preferences, username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("update user_info set preferences={} where username={}".format("'" + preferences + "'","'" + username + "'"))

    db.commit()
    db.close()

def check_recipe(user, recipe_name):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    for entry in c.execute("SELECT user, title FROM recipes"):
        if(entry[0] == user and entry[1] == recipe_name):
            db.close()
            return True

    db.close()
    return False

def get_user_recipes(user):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    recipes = []

    for i in c.execute("select * from recipes where user ={}".format("'" + user + "'")):
        recipes.append(i)

    return recipes


def remove_recipe(user, recipe_name):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute("DELETE FROM recipes WHERE user={} AND title={}".format("'" + user + "'", "'" + recipe_name + "'"))

    db.commit()
    db.close()


# def printstuff():
#     db = sqlite3.connect(DB_FILE)
#     c = db.cursor()

#     for i in c.execute("select ingredients from recipes where user='admin'"):
#         hi = i[0].split("\r\n")
#         print(hi)

#     db.close()

# printstuff()
# get_preference("admin")
# create_tables()

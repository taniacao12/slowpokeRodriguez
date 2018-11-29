import sqlite3

DB_FILE="discobandit.db" # db used for this project. delete file if you want to remove all data/login info.

db = sqlite3.connect(DB_FILE) # Open if file exists, otherwise create

def create_tables():
    c = db.cursor()

    c.execute("CREATE TABLE if not exists user_info(user TEXT PRIMARY KEY, password TEXT, preferences TEXT)")
    c.execute("CREATE TABLE if not exists recipes(user TEXT, title TEXT, ingredients TEXT, instructions TEXT, images TEXT)")

    db.commit()

    db.close()

    


# create_tables()
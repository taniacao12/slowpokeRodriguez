import sqlite3

DB_FILE="discobandit.db" # db used for this project. delete file if you want to remove all data/login info.


def create_tables():
    db = sqlite3.connect(DB_FILE) # Open if file exists, otherwise create
    c = db.cursor()

    c.execute("CREATE TABLE if not exists user_info(user TEXT PRIMARY KEY, password TEXT, preferences TEXT)")
    c.execute("CREATE TABLE if not exists recipes(user TEXT, title TEXT, ingredients TEXT, instructions TEXT, images TEXT)")

    db.commit()

    db.close()

def add_user(username, password):
    ''' insert credentials for newly registered user into database '''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES(?, ?, ?)", (username, password, "none"))
    db.commit() #save changes
    db.close() #close database

    


# create_tables()

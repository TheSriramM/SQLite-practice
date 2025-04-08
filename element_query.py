import sqlite3

DATABASE = "elements.db"

while True:
    try:
        atomic_mass = input("Greater than what atomic mass? ")
        db = sqlite3.connect(DATABASE)
        #can replace above line with with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        #don't use a f string or concatenate the variable because of sql injections
        query = "SELECT name, atomic_mass FROM elements WHERE atomic_mass > ?;"
        cursor.execute(query, tuple(atomic_mass))
        results = cursor.fetchall()
        #print each element on a seperate line
        results = [print(element) for element in results]
        db.close()
        break
    except ValueError:
        print("Please enter a valid input.")

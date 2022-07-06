import sqlite3

db = sqlite3('cookbook.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS food(
    ingredients TEXT,
    cuisine TEXT,
    diet TEXT
    )""")

db.commit()

food_ingredients = input("Ingredients: ")
food_cuisine = input("Cuisine: ")
food_diet = input("Diet: ")

sql.execute("SELECT ingredients FROM  food")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO food VALUES (?)", (food_ingredients))
    db.commit()
else:
    print("Ingredients are available")

    sql.execute("SELECT cuisine FROM  food")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO food VALUES (?)", (food_cuisine))
        db.commit()
    else:
        print("Cuisine are available")

        sql.execute("SELECT diet FROM food")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO food VALUES(?)", (food_diet))
            db.commit()
        else:
            print("Diet are available")
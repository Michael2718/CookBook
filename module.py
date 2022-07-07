# import sqlite3
#
# db = sqlite3('cookbook.db')
# sql = db.cursor()
#
# sql.execute("""CREATE TABLE IF NOT EXISTS food(
#     ingredients TEXT,
#     cuisine TEXT,
#     diet TEXT
#     )""")
#
# db.commit()
#
# food_ingredients = input("Ingredients: ")
# food_cuisine = input("Cuisine: ")
# food_diet = input("Diet: ")
#
# sql.execute("SELECT ingredients FROM  food")
# if sql.fetchone() is None:
#     sql.execute(f"INSERT INTO food VALUES (?)", (food_ingredients))
#     db.commit()
# else:
#     print("Ingredients are available")
#
#     sql.execute("SELECT cuisine FROM  food")
#     if sql.fetchone() is None:
#         sql.execute(f"INSERT INTO food VALUES (?)", (food_cuisine))
#         db.commit()
#     else:
#         print("Cuisine are available")
#
#         sql.execute("SELECT diet FROM food")
#         if sql.fetchone() is None:
#             sql.execute(f"INSERT INTO food VALUES(?)", (food_diet))
#             db.commit()
#         else:
#             print("Diet are available")

import sqlite3

database = sqlite3.connect("database.db")
cursor = database.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    login TEXT,
    password TEXT
)""")

database.commit()

if input("Sign in or Sign up? " "1 or 2: ") == "1":
    login = input("Login: ")

    cursor.execute(f"SELECT login FROM users WHERE login = '{login}'")
    if not cursor.fetchone() is None:
        password = input("Password: ")

        cursor.execute(f"SELECT login, password FROM users WHERE login = '{login}'")
        if cursor.fetchone()[1] == password:
            print("You are logged in! ")  # вы вошли в систему
        else:
            print("Incorrect password")  # неверный пароль

else:
    inp_login = input("Login: ")
    inp_password = input("Password: ")

    cursor.execute(f"SELECT login FROM users WHERE login = '{inp_login}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (inp_login, inp_password))

        database.commit()
    else:
        print("Such a login exists! ")  # такой логин существует

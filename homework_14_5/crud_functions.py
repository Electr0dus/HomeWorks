import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')
    connection.commit()


def is_include(username):
    users = cursor.execute(f"SELECT username FROM Products").fetchall()
    new_list = []
    for us in users:
        new_list += us
    print(new_list)
    if username in new_list:
        return True
    else:
        return False


def add_user(username, email, age):
    if is_include(username):
        return 0
    else:
        cursor.execute("INSERT INTO Products (username, email, age, balance) VALUES (?,?,?,?)",
                       (username, email, age, 1000))
        connection.commit()

def get_all_products():
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    return data




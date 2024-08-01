import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );
    ''')
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    connection.close()
    return data


# initiate_db()
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (id, title, description, price) VALUES(?, ?, ?, ?)", (i, f"Продукт {i}",
#                                                                                                f'Описание {i}',
#                                                                                                i * 100,))
# print(get_all_products())
# connection.commit()

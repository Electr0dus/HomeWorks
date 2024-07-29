import sqlite3

conn = sqlite3.connect('not_telegram.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


for i in range(1, 11):
    cursor.execute("INSERT INTO Users (id, username, email, age, balance) VALUES (?, ?, ?, ?, ?)",
                   (f'{i}', f'User{i}', f'example{i}@gmail.com', f'{i * 10}', f'{1000}'))


for i in range(1, 11):
    if i % 2 == 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, i,))
    else:
        continue


for i in range(1, 11):
    if i % 3 == 0:
        cursor.execute("DELETE FROM Users WHERE id = ?", (i,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))

users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

conn.commit()
conn.close()

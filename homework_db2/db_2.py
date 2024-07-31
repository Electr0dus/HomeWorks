import sqlite3

conn = sqlite3.connect('not_telegram.db')

cursor = conn.cursor()

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT id FROM Users")

id = cursor.fetchall()
print(f'Общее кол-во записей = {len(id)}')


cursor.execute("SELECT balance FROM Users")

balance = cursor.fetchall()
count = 0
for all_b in balance:
    count+= all_b[0]

print(f'Общий баланс равен: {count}')
print(f'Средний баланс равен {count/len(id):.2f}')
conn.commit()
conn.close()

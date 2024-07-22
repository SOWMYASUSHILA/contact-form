import sqlite3

conn = sqlite3.connect('contact.db')
c = conn.cursor()
c.execute('SELECT * FROM contacts')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()

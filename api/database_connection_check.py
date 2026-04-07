import sqlite3

DATABASE = "users.db"

def get_db_connection():
    conn =sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
users = conn.execute("SELECT * FROM users").fetchall()
conn.close()

for i in users:
    print(dict(i))
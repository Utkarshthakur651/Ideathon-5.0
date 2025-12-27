import sqlite3

DB_NAME="tasks.db"

conn=sqlite3.connect(DB_NAME,check_same_thread=False)

data={}

crs=conn.cursor()
crs.execute("""CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
            )
        """)

crs.execute("INSERT INTO tasks (task, done) VALUES(?,0)",())

conn.commit()
conn.close()
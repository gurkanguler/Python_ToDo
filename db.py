import sqlite3

conn = sqlite3.connect("db.db")

cur = conn.cursor()


cur.execute("CREATE TABLE user(id INTEGER PRIMARY KEY NOT NULL,name TEXT,password TEXT,todo TEXT)")

cur.execute("INSERT INTO user(name,password,todo) VALUES('test','test','test')")

conn.commit()

import sqlite3 as sql 

def database_connection():
    return sql.connect("database.db" , check_same_thread=False)

def Create_Users():
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Tasky_Users 
    (id INTEGER PRIMARY KEY AUTOINCREMENT  ,
    name TEXT UNIQUE , 
    email TEXT UNIQUE , 
    password TEXT) ''')
    connection.commit()
    connection.close()
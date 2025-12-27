import streamlit as st 
import sqlite3 as sql
from database import database_connection
import hashlib as hash 

def hash_pass(password):
    return hash.sha256(password.encode()).hexdigest()



def signup(name , email , password):
    connection = database_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''
        INSERT INTO Tasky_Users (name , email , password) VALUES (? , ? , ?)''' 
        , (name , email , hash_pass(password)) )
        connection.commit()
        return True
    except sql.IntegrityError:
        return False
    finally :
        connection.close()
                       
def login(email , password):
    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Tasky_Users WHERE email = ? AND password = ?",(email , hash_pass(password)))                    
    user = cursor.fetchone()
    connection.close()
    return user 














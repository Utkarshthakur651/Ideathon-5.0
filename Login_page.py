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






















# for i in range(5) :
#     st.write("            ")

# col1 , col2 = st.columns(2)
# with col1 :
#     st.header(":green[New User]")
#     sign_up_button = st.button(":blue[Sign Up]")

# with col2 :
#     st.header(":green[Existing User]")
#     sign_in_button = st.button(":blue[Sign In]")


# def add_info(a,b,c,d):
#     connection.execute('''
# CREATE TABLE IF NOT EXISTS Tasky_db (name TEXT(20) , last_name TEXT(15) , mail_id TEXT(40) UNIQUE PRIMARY KEY ,password TEXT(15)                            
#                    ''')
#     connection.execute("INSERT INTO Tasky_db VALUES(/ , / , / , /)".format(a,b,c,d))
#     connection.commit()
#     connection.close()

#     st.success("User has been added to the sqlite database successfully .")

# def create_signup_form():
#     st.write("Enter your details :")
#     with st.form(key = "Sign Up form :"):
#         name = st.text_input("Enter your name :")
#         last_name = st.text_input("Enter your last name :")
#         mail_id = st.text_input("Enter your Email Address :" )
#         password = st.text_input("Enter the Password for your Account :" , key = "password")
#         submit1 = st.form_submit_button(label= "Register")
#         if submit1 :
#             st.success("You are now a part of Tasky Family 😊")
#             add_info(name , last_name , mail_id , password)

# def create_signin_form():
#     st.write("Enter your details :")
#     with st.form(key = "Sign In form :"):
#         name = st.text_input("Enter your name :")
#         last_name = st.text_input("Enter your last name :")
#         mail_id = st.text_input("Enter your Email Address :")
#         password = st.text_input("Enter the Password for your Account :" , key ="password")
#         submit2 = st.form_submit_button(label= "Sign In")
#         if submit2 :
#             st.success("You have been signed in , Have a Productive Day ahead ✌️")
#             add_info(name , last_name , mail_id , password)

# if sign_up_button :
#     create_signup_form()

# elif sign_in_button :
#     create_signin_form()
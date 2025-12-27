import streamlit as st 
import sqlite3 as sql 
import hashlib as hash

st.set_page_config(page_title= "Tasky Login " , page_icon="🔒" , layout="wide")

# def database_connection():
#     connection = sql.connect("database.db")
#     connection.row_factory = sql.Row
#     return connection

con = sql.connect("database.db")
cursor = con.cursor()
# cursor.execute(''' CREATE TABLE IF NOT EXISTS demo ( id INT AUTO_INCREMENT PRIMARY KEY , 
#                name TEXT(15) NOT NULL , mail TEXT(20) UNIQUE NOT NULL 
#                , password TEXT(10) UNIQUE NOT NULL )''')
# cursor.execute("INSERT INTO demo VALUES(2 ,'vansh' , 'vardaanabbi20@gmail.com' , 'vansh.abbi@2005' )")
cursor.execute("SELECT * FROM demo ")
cursor.fetchall()
con.commit()
con.close()





















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
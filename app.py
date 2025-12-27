import streamlit as st
import sqlite3

#Install SQLite by alexcvzz extension in vscode

DB_NAME="tasks.db"

def get_connection():
    return sqlite3.connect(DB_NAME,check_same_thread=False)

def init_db():
    conn=get_connection()
    crs=conn.cursor()
    crs.execute("""CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
                )
            """)
    conn.commit()
    conn.close()

def add_task(task):
    conn=get_connection()
    crs=conn.cursor()
    crs.execute("INSERT INTO tasks (task, done) VALUES(?,0)",(task,))
    conn.commit()
    conn.close()

def get_tasks():
    conn=get_connection()
    crs=conn.cursor()
    crs.execute("SELECT id,task,done FROM tasks")
    tasks=crs.fetchall()
    conn.commit()
    conn.close()
    return tasks

def update_task(id,done):
    conn=get_connection()
    crs=conn.cursor()
    crs.execute("UPDATE tasks SET done=? WHERE id=?",(done,id))
    tasks=crs.fetchall()
    conn.commit()
    conn.close()
#----------------------------App Initialisation--------------------------
st.title("Task Manager")
st.caption("Simple. Persistent. No excuses.")

init_db()

with st.form("add_task_form"):
    new_task=st.text_input("New task")
    submitted=st.form_submit_button("Add")

    if submitted and new_task.strip():
        add_task(new_task)
        st.rerun()

st.divider()

tasks=get_tasks()
if not tasks:
    st.info("No tasks yet. Add one.")
else:
    for id,task,done in tasks:
        col1,col2,co3=st.columns([0.1,0.7,0.2])

        with col1:
            checked=st.checkox("",value=bool(done),key=f"check_(id)")
        
            if checked!=bool(done):
                update_task(id,int(checked))
                st.rerun()
        

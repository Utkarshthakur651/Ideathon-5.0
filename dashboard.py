import streamlit as st
import time
import sqlite3
from datetime import date

# DATABASE
conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT UNIQUE,
    deadline TEXT,
    priority INTEGER,
    task_status INTEGER DEFAULT 0
)
""")
conn.commit()
#------------------------------------------------------------------------

#SESSION STATE 
defaults = {
    "animated": False,
    "page": "Welcome",
    "current_task": 1,
    "tasks_data": {},
    "error": "",
    "edit_id": None
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v
#---------------------------------------------------------------------

# BACKGROUND (CSS)
st.markdown("""
<style>
.stApp { background: #ffffff; font-family: 'Inter', sans-serif; }

h1 { font-size: 52px !important; font-weight: 900; color: #2563eb; }
h2 { font-size: 32px; font-weight: 800; }
h3 { font-size: 26px; font-weight: 700; }

label { font-size: 22px; font-weight: 700; }

div.stButton > button {
    background-color: #2563eb;
    color: white;
    font-weight: 700;
    font-size: 18px;
    border-radius: 12px;
    padding: 12px 30px;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR 
st.sidebar.markdown("## 📊 Dashboard")
menu = st.sidebar.radio("", ["Home", "Add Task", "My Tasks", "Edit Task"])
st.session_state.page = menu
#-------------------------------------------------------------------------------------------

#  WELCOME 
if st.session_state.page == "Home":
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)

    if not st.session_state.animated:
        placeholder = st.empty()
        text = "✨ Welcome to Tasky✨"
        typed = ""
        for ch in text:
            typed += ch
            placeholder.markdown(f"# {typed}")
            time.sleep(0.05)
        st.session_state.animated = True
    else:
        st.markdown("# ✨ Welcome to Tasky✨")

    st.markdown("""
    ### 🚀 Plan • Organize • Achieve
    ✔ Add tasks  
    ✔ Track deadlines  
    ✔ Edit easily  
    ✔ Mark tasks as done  
    """)
    st.markdown("</div>", unsafe_allow_html=True)
#-------------------------------------------------------------------------------

#  ADD TASK 
elif st.session_state.page == "Add Task":
    i = st.session_state.current_task
    st.markdown(f"## ➕ Add Task {i}")

    task = st.text_input("📝 Task Description", key=f"task_{i}")
    deadline = st.date_input("📅 Deadline", min_value=date.today(), key=f"date_{i}")
    priority = st.slider("🔥 Priority", 1, 5, key=f"diff_{i}")

    if st.session_state.error:
        st.error(st.session_state.error)

    col1, col2, col3 = st.columns(3)

    with col1:
        if i > 1 and st.button("⬅ Previous"):
            st.session_state.current_task -= 1
            st.session_state.error = ""
            st.rerun()

    with col2:
        if st.button("Next ➡"):
            if task.strip() == "":
                st.session_state.error = "❌ Task cannot be empty"
            elif task in [t["task"] for t in st.session_state.tasks_data.values()]:
                st.session_state.error = "❌ Duplicate task not allowed"
            else:
                st.session_state.tasks_data[i] = {
                    "task": task,
                    "deadline": deadline,
                    "priority": priority
                }
                st.session_state.current_task += 1
                st.session_state.error = ""
                st.rerun()

    with col3:
        if st.button("✅ Submit"):
            if task.strip() == "":
                st.session_state.error = "❌ Task cannot be empty"
            elif task in [t["task"] for t in st.session_state.tasks_data.values()]:
                st.session_state.error = "❌ Duplicate task not allowed"
            else:
                st.session_state.tasks_data[i] = {
                    "task": task,
                    "deadline": deadline,
                    "priority": priority
                }

                for t in st.session_state.tasks_data.values():
                    try:
                        cursor.execute(
                            "INSERT INTO tasks (task, deadline, priority) VALUES (?, ?, ?)",
                            (t["task"], str(t["deadline"]), t["priority"])
                        )
                    except:
                        pass
                conn.commit()

                st.success("🎉 Tasks added successfully!")
                st.session_state.tasks_data = {}
                st.session_state.current_task = 1
                st.session_state.page = "My Tasks"
                st.rerun()
#--------------------------------------------------------------------------------------------------------------------

#  MY TASKS
elif st.session_state.page == "My Tasks":
    st.markdown("## 📋 My Tasks")

    cursor.execute("SELECT id, task, deadline, priority , task_status FROM tasks")
    rows = cursor.fetchall()

    if not rows:
        st.info("No tasks yet.")
    else:
        for tid, task, deadline, priority , task_status in rows:
            status = "✅ Done" if task_status else "⏳ Pending"
            st.markdown(f"""
            ### 📝 {task}
            **📅 Deadline:** {deadline}  
            **🔥 Priority:** {priority}  
            **📌 Status:** {status}
            """)

            if not task_status :
                if st.button("✔ Mark as Done", key=f"done_{tid}"):
                    cursor.execute("UPDATE tasks SET done=1 WHERE id=?", (tid,))
                    conn.commit()
                    st.rerun()
            st.divider()
#---------------------------------------------------------------------------------------------------------------------

# EDIT TASK 
elif st.session_state.page == "Edit Task":
    st.markdown("## ✏️ Edit Tasks")

    cursor.execute("SELECT id, task, deadline, priority FROM tasks WHERE task_status=0")
    rows = cursor.fetchall()

    if not rows:
        st.info("No editable tasks available.")
    else:
        for tid, task, deadline, priority in rows:
            with st.expander(f"✏️ Edit: {task}"):
                new_task = st.text_input("Task", task, key=f"et_{tid}")
                new_deadline = st.date_input("Deadline", date.fromisoformat(deadline), key=f"ed_{tid}")
                new_priority = st.slider("Difficulty", 1, 5, priority , key=f"ef_{tid}")

                if st.button("💾 Update Task", key=f"up_{tid}"):
                    try:
                        cursor.execute("""
                            UPDATE tasks
                            SET task=?, deadline=?, priority=?
                            WHERE id=?
                        """, (new_task, str(new_deadline), new_priority, tid))
                        conn.commit()
                        st.success("✅ Task updated!")
                        st.rerun()
                    except:
                        st.error("❌ Duplicate task not allowed")

#-----------------------------------------------------------------------------------------------------------------------

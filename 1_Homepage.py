import streamlit as st 

st.set_page_config(
    page_title="TASKY" , 
    page_icon= "✅" ,
    layout= "wide"
)
st.title("✅TASKY")
st.caption("Plan Smart . Finish Faster")

st.markdown("")

if "show_login" not in st.session_state :
    st.session_state.show_login = False

st.markdown('''
<h1 style= 'margin-bottom: 6px; font-weight: Bold;'>PRIORITIZE WHAT</h1>
<h1 style= 'margin-top: 12px; color: blue; font-weight: Bold;'>MATTERS MOST.</h>''' , unsafe_allow_html=True)

st.write("### :grey[ Smart Task prioritizer powered by deadline urgency "
"and intensity levels . Get automatic prioritization , visual roadmaps and email " \
"reminders to stay on top of your work.]")

 
if st.button("Sign-Up/Sign-In") :
    st.session_state.show_login = True

st.image("https://imgs.search.brave.com/7tzPh-SwK6fXjCzdSftWXJ0rds7hfcsMLpnkaHLmq68/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9nbG9h/dC5jb20vd3AtY29u/dGVudC91cGxvYWRz/L3NodXR0ZXJzdG9j/a18yNDU1MjM5NTY5/LmpwZw", width= 800)
st.sidebar.success("Select a page above")
st.markdown("<p style = 'text-align: center; font-family: Times New Roman ; font-size: 35px; font-weight: Bold'>Everything you need to Stay Organized</p>" , unsafe_allow_html=True)
st.markdown("<p style = 'text-align: center; font-family: Times New Roman ; font-size: 22px; color: gray'> Powerful features designed for productivity professionals</p>" , unsafe_allow_html=True)

st.markdown("_ _ _")

st.markdown("""
<style>
.feature-card {
    text-align: left;
    padding: 30px 20px;
            width: 100%;
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 12px;
}

.feature-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
}

.feature-desc {
    font-size: 14px;
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# Create 4 columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">Smart Prioritization</div>
        <div class="feature-desc">
            Automatic task ranking based on deadline urgency and intensity levels
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📅</div>
        <div class="feature-title">Visual Roadmap</div>
        <div class="feature-desc">
            Timeline view showing all your tasks in a Gantt-style layout
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📧</div>
        <div class="feature-title">Email Reminders</div>
        <div class="feature-desc">
            On-demand email notifications to keep you on track
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <div class="feature-title">Progress Tracking</div>
        <div class="feature-desc">
            Real-time statistics and insights on your task completion
        </div>
    </div>
    """, unsafe_allow_html=True)

import streamlit as st

st.markdown("""
<style>
/* Target all Streamlit buttons */
div.stButton > button {
    background-color: #2563eb;   /* Blue background */
    color: white;                /* Text color */
    font-size: 16px;
    font-weight: 600;
    border-radius: 10px;
    padding: 10px 24px;
    border: none;
}

/* Hover effect */
div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("_ _ _")
st.markdown("<p style = 'text-align: left; font-family: Times New Roman; font-size: 30px; font-weight: Bold'>Ready to Take Control of Your Tasks ?</p>" , unsafe_allow_html=True )
st.write("<p style = 'text-align: right ; font-family: Times New Roman ; font-color: gray; font-size: 20px '>Join professionals who prioritize effectively and get more done</p>" , unsafe_allow_html=True)
st.markdown("")

col5 , col6 , col7 = st.columns([1,2,1])


with col6 :
    if st.button("### **Start Prioritizing Today**" , width = 300):
        st.session_state.show_login = True

if st.session_state.show_login :
    @st.dialog("Welcome Back")
    def login_popup():
        tab1 , tab2 = st.tabs(["New User" , "Existing User"])

        with tab1 :
            name = st.text_input("Name" , key="name" , type="default")
            email = st.text_input("Email" , key= "sign-up_email")
            password = st.text_input("Password" , type="password" , key="sign-up_pass")

            if st.button("Sign-Up"):
                st.success("Account Created Successfully !")
                st.session_state.show_login = False
                st.rerun()


        with tab2 :
            email = st.text_input("Email" , key="login_email")
            password = st.text_input("Password" , type="password" , key="login_pass")
            if st.button("Sign-In"):
                st.success("Signed In Successfully")
                st.session_state.show_login = False
                st.rerun()


    login_popup()
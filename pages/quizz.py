import streamlit as st
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="Central Hub | QuizForge", page_icon="🧬", layout="wide")
set_page_style()

# Page-Specific Styling for Hub Buttons
st.markdown("""
<style>
    /* Target the first column's button (Student Hub) */
    [data-testid="stColumn"]:nth-of-type(1) .stButton > button {
        background: linear-gradient(135deg, #10B981, #065F46) !important;
        color: white !important;
        border: none !important;
        text-align: center !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
    }
    
    /* Target the second column's button (Admin Hub) */
    [data-testid="stColumn"]:nth-of-type(2) .stButton > button {
        background: linear-gradient(135deg, #EF4444, #9E1A1A) !important;
        color: white !important;
        border: none !important;
        text-align: center !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 QUIZFORGE CENTRAL HUB")
st.markdown("### THE ULTIMATE NEURAL ASSESSMENT PORTAL")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    with st.container(border=True):
        st.markdown("<h2 style='color: var(--accent); margin: 0; padding: 0;'>👨‍🎓 Student Hub</h2>", unsafe_allow_html=True)
        st.markdown("<p style='height: 50px; margin: 10px 0;'>Configure neural assessment parameters and verify efficiency.</p>", unsafe_allow_html=True)
        if st.button("INITIALIZE STUDENT PORTAL", key="init_student", use_container_width=True):
            st.switch_page("pages/student_hub.py")

with col2:
    with st.container(border=True):
        st.markdown("<h2 style='color: var(--red-accent); margin: 0; padding: 0;'>⚙️ Admin Hub</h2>", unsafe_allow_html=True)
        st.markdown("<p style='height: 50px; margin: 10px 0;'>Access central question nodes and maintain system integrity.</p>", unsafe_allow_html=True)
        if st.button("ACCESS ADMIN PORTAL", key="init_admin", use_container_width=True):
            st.switch_page("pages/admin.py")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div id="violet-marker"></div>', unsafe_allow_html=True)
if st.button("← RETURN TO LANDING"):
    st.switch_page("app.py")

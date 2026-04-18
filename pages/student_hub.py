import streamlit as st
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="Student Portal | QuizForge", page_icon="👨‍🎓", layout="wide")
set_page_style()

# Page-Specific Styling for Student Portal
st.markdown("""
<style>
    /* Green buttons for Topic Selection (inside columns) still use column targeting */
    [data-testid="stColumn"] .stButton > button {
        background: linear-gradient(135deg, #10B981, #065F46) !important;
        color: white !important;
        border: none !important;
        text-align: center !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Session Check
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

st.title("👨‍🎓 STUDENT PORTAL HUB")
st.markdown("### CONFIGURE YOUR NEURAL ASSESSMENT PARAMETERS")

st.markdown('<div class="portal-card-student" style="padding-top: 1rem;">', unsafe_allow_html=True)
st.header("⚙️ Node Configuration")

# Identification Tag
user_name = st.text_input("Identity Tag (Required):", 
                         value=st.session_state.get('user_name', ''),
                         placeholder="e.g. USER-774")

# Topic Selection
st.write("### 🧬 Select Neural Node")
c1, c2, c3 = st.columns(3)

topics = [
    {"id": "Science", "icon": "🧪"}, # Emerald Green Icon
    {"id": "Math", "icon": "📐"},    # Green/Yellow Icon
    {"id": "History", "icon": "📜"}  # Amber Icon
]

selected_topic = st.session_state.get('selected_topic', None)

for i, t in enumerate(topics):
    with [c1, c2, c3][i]:
        is_selected = selected_topic == t['id']
        style_class = "topic-selected" if is_selected else ""
        
        st.markdown(f"""
        <div class="topic-card {style_class}">
            <div style="font-size: 3rem; margin-bottom: 10px;">{t['icon']}</div>
            <div style="font-size: 1.6rem; font-weight: bold; font-family: 'Orbitron';">{t['id']}</div>
            <div style="opacity: 0.6; font-size: 0.85rem;">ACTIVE PORTAL NODE</div>
            {"<div style='color: white; font-weight: bold; margin-top: 10px;'>✓ LOCKED</div>" if is_selected else ""}
        </div>
        """, unsafe_allow_html=True)
        if st.button(f"SELECT {t['id']}", key=f"sel_{t['id']}", use_container_width=True):
            st.session_state['selected_topic'] = t['id']
            st.rerun()

st.divider()

# Session Parameters
col_a, col_b = st.columns(2)
with col_a:
    q_count = st.selectbox("Batch Count:", [4, 6, 8, 10], index=0)
with col_b:
    t_per_q = st.selectbox("Latency Limit (Sec):", ["10S", "15S", "20S"], index=0)

st.markdown('</div>', unsafe_allow_html=True)

# Launch Execution
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div id="green-marker"></div>', unsafe_allow_html=True)
if st.button("🚀 BEGIN NEURAL ASSESSMENT"):
    if not user_name:
        st.error("Protocol Error: Identity Tag Required.")
    elif not selected_topic:
        st.error("Protocol Error: Neural Node Selection Required.")
    else:
        st.session_state['user_name'] = user_name
        st.session_state['config_topic'] = selected_topic
        st.session_state['config_count'] = q_count
        st.session_state['config_time'] = int(t_per_q[:-1])
        st.session_state.pop('quiz_initialized', None)
        st.switch_page("pages/exam_session.py")

st.markdown('<div id="red-marker"></div>', unsafe_allow_html=True)
if st.button("← RETURN TO HUB"):
    st.switch_page("pages/quizz.py")

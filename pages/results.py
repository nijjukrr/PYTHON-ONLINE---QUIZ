import streamlit as st
import pandas as pd
from utils.ui_components import set_page_style

# Initialize Page
st.set_page_config(page_title="Performance Sync | QuizForge", page_icon="📊", layout="wide")
set_page_style()

# Session Check
if 'user_name' not in st.session_state:
    st.switch_page("app.py")

# Metrics Calculation
questions = st.session_state['questions']
answers = st.session_state['answers']
score = st.session_state['score']
total = len(questions)
accuracy = (score / total) * 100
correct_count = score
wrong_count = sum(1 for a, q in zip(answers, questions) if a and a != q['answer'])
skipped_count = sum(1 for a in answers if a is None)
points = score * 10
max_points = total * 10

st.title("🎯 PERFORMANCE SYNCHRONIZATION")
st.markdown("### NEURAL EFFICIENCY ANALYSIS COMPLETE")

# Results Layout (Circular Chart + 2x2 Grid)
col_l, col_r = st.columns([1, 1], gap="large")

with col_l:
    # Circular Points Chart
    st.markdown(f"""
    <div class="score-container">
        <div style="font-family: 'Orbitron'; margin-bottom: 15px; letter-spacing: 2px; font-size: 1.2rem;">📊 RESULTS</div>
        <div class="score-circle" style="--percentage: {accuracy}%">
            <div class="score-inner">
                <div class="score-value">{points}</div>
                <div class="score-label">POINTS</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    # 2x2 Metric Grid
    st.markdown(f"""
    <div class="result-grid">
        <div class="stat-card">
            <div class="stat-val" style="color: var(--accent);">{correct_count}</div>
            <div class="stat-label">CORRECT</div>
        </div>
        <div class="stat-card">
            <div class="stat-val" style="color: var(--red-accent);">{wrong_count}</div>
            <div class="stat-label">WRONG</div>
        </div>
        <div class="stat-card">
            <div class="stat-val" style="color: #FBB03B;">{skipped_count}</div>
            <div class="stat-label">SKIPPED</div>
        </div>
        <div class="stat-card">
            <div class="stat-val" style="color: var(--neural-timer);">{max_points}</div>
            <div class="stat-label">MAX PTS</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Action Buttons
btn_c1, btn_c2 = st.columns([1, 1])
with btn_c1:
    if st.button("🔄 RETRY SESSION", use_container_width=True):
        for key in ['quiz_initialized', 'questions', 'answers', 'feedback', 'current_idx', 'score']:
            if key in st.session_state: del st.session_state[key]
        st.switch_page("pages/student_hub.py")

with btn_c2:
    st.markdown('<div class="neural-btn">', unsafe_allow_html=True)
    if st.button("🏆 LEADERBOARD", use_container_width=True):
        st.switch_page("pages/leaderboard.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div id="red-marker"></div>', unsafe_allow_html=True)
if st.button("← RETURN TO HUB", use_container_width=True):
    # Clear session for fresh start
    for key in ['quiz_initialized', 'questions', 'answers', 'feedback', 'current_idx', 'score']:
        if key in st.session_state: del st.session_state[key]
    st.switch_page("pages/quizz.py")

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# ANSWER REVIEW SECTION (Image 4 Sync)
st.markdown("## 📑 Answer Review")

for i, q in enumerate(questions):
    with st.container(border=True):
        st.markdown(f'<div style="font-family: Inter; font-weight: bold; margin-bottom: 15px; font-size: 1.1rem; color: #EEEEEE;">Q{i+1}. {q["question"]}</div>', unsafe_allow_html=True)
        
        user_ans = answers[i] if answers[i] else "No Response"
        correct_ans = q['answer']
        
        # Pill Display
        if user_ans == correct_ans:
            st.markdown(f'<span class="quiz-pill pill-correct">✓ Your: {user_ans}</span>', unsafe_allow_html=True)
        else:
            p_html = f"""
            <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                <span class="quiz-pill pill-wrong">✕ Your: {user_ans}</span>
                <span class="quiz-pill pill-correct" style="background: rgba(6, 182, 212, 0.1); color: #06B6D4; border-color: rgba(6, 182, 212, 0.2);">✓ Correct: {correct_ans}</span>
            </div>
            """
            st.markdown(p_html, unsafe_allow_html=True)

# Leaderboard recording logic (kept as is)
if 'leaderboard_saved' not in st.session_state:
    try:
        df = pd.read_csv("data/leaderboard.csv")
    except:
        df = pd.DataFrame(columns=["User", "Topic", "Score", "Accuracy", "Timestamp"])
    
    new_entry = {
        "User": st.session_state.get('user_name', 'Unknown'),
        "Topic": st.session_state.get('config_topic', 'General'),
        "Score": score,
        "Accuracy": f"{accuracy:.1f}%",
        "Timestamp": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv("data/leaderboard.csv", index=False)
    st.session_state['leaderboard_saved'] = True

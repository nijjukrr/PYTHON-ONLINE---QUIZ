import streamlit as st
import time
from utils.ui_components import set_page_style
from utils.question_loader import load_questions_to_set

# Initialize Page
st.set_page_config(page_title="Neural Session | QuizForge", page_icon="⚡", layout="wide")
set_page_style()

# Session Check
if 'user_name' not in st.session_state:
    st.switch_page("app.py")

# Initialization Logic
if 'quiz_initialized' not in st.session_state:
    st.session_state['quiz_initialized'] = True
    st.session_state['questions'] = load_questions_to_set(
        "data/question_bank.json", 
        st.session_state['config_topic'], 
        "Easy", 
        st.session_state['config_count']
    )
    st.session_state['answers'] = [None] * len(st.session_state['questions'])
    st.session_state['feedback'] = [None] * len(st.session_state['questions'])
    st.session_state['current_idx'] = 0
    st.session_state['q_start_time'] = time.time()
    st.session_state['score'] = 0

questions = st.session_state['questions']
idx = st.session_state['current_idx']
q_item = questions[idx]

# TOP BAR: [Label] --- [Timer] --- [Submit] (Image 2 Sync)
col_l, col_c, col_r = st.columns([1, 1, 1])

with col_l:
    st.markdown(f'<div style="color: rgba(255,255,255,0.6); font-family: Inter; font-size: 0.9rem;">Q {idx + 1} of {len(questions)} • {st.session_state["config_topic"]}</div>', unsafe_allow_html=True)
    st.progress((idx + 1) / len(questions))

limit = st.session_state['config_time']
elapsed = time.time() - st.session_state['q_start_time']
remaining = max(0, int(limit - elapsed))

with col_c:
    # Single-unit holographic timer
    st.markdown(f'<div style="text-align: center; font-family: Orbitron; font-size: 2.2rem; color: var(--neural-timer); letter-spacing: 2px;">00:{remaining:02d}</div>', unsafe_allow_html=True)

with col_r:
    st.markdown('<div style="text-align: right; transform: translateY(-5px);">', unsafe_allow_html=True)
    if st.button("Submit All", key="submit_all_top", use_container_width=False):
        st.switch_page("pages/results.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# MAIN QUESTION CARD (Image 2 Sync)
with st.container(border=True):
    # Header row inside card
    card_h1, card_h2 = st.columns([1, 1])
    with card_h1:
        st.markdown(f'<div style="color: rgba(255,255,255,0.5); font-size: 0.8rem; font-weight: bold; font-family: Inter;">QUESTION {idx + 1}</div>', unsafe_allow_html=True)
    with card_h2:
        st.markdown(f'<div style="text-align: right;"><span class="quiz-pill pill-score">+10 pts</span></div>', unsafe_allow_html=True)
    
    st.markdown(f'<h2 style="font-family: Inter; margin-top: 10px; color: white;">{q_item["question"]}</h2>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    labels = ["A", "B", "C", "D"]
    res = st.session_state['feedback'][idx]
    user_choice = st.session_state['answers'][idx]
    correct_ans = q_item['answer']

    # OPTION GRID rendering
    for i, opt in enumerate(q_item['options']):
        # Determine status
        style = ""
        icon = ""
        if res is not None:
            if opt == correct_ans:
                style = "correct-opt"
                icon = "✓"
            elif opt == user_choice and res != "Correct":
                style = "wrong-opt"
                icon = "✕"
        
        # We use a button for selection, but we want it to look like a card.
        # So we embed the HTML card look, but with the button inside or as the trigger.
        # But Streamlit buttons can't contain complex HTML.
        # So we use the "div-over-button" trick or just better button styling.
        # Here we'll use the button for interactivity if no result, 
        # else just the div for feedback.
        
        if res is None:
            # INTERACTIVE STATE: Buttons that look like the cards in the photo
            if st.button(f"{labels[i]} &nbsp;&nbsp;&nbsp; {opt}", key=f"btn_{idx}_{i}", use_container_width=True):
                st.session_state['answers'][idx] = opt
                is_correct = opt == q_item['answer']
                st.session_state['feedback'][idx] = "Correct" if is_correct else "Incorrect"
                if is_correct: st.session_state['score'] += 1
                st.rerun()
        else:
            # FEEDBACK STATE: HTML as shown in Image 2/3
            st.markdown(f"""
            <div class="quiz-option-card {style}">
                <div style="display: flex; align-items: center;">
                    <div class="letter-marker">{labels[i]}</div>
                    <div style="font-family: Inter; color: white;">{opt}</div>
                </div>
                <div style="font-weight: bold; font-size: 1.2rem; color: { 'var(--accent)' if style == 'correct-opt' else 'var(--red-accent)' if style == 'wrong-opt' else 'white' };">{icon}</div>
            </div>
            """, unsafe_allow_html=True)

# FOOTER NAVIGATION (Image 2/3 Sync)
st.markdown("<br>", unsafe_allow_html=True)
f_col1, f_col2 = st.columns([2, 1])

with f_col1:
    # Pagination Nodes - Circular indicators as seen in Image 2
    st.markdown('<div class="pagination-container">', unsafe_allow_html=True)
    cols = st.columns(min(len(questions), 10)) # Cap at 10 for width safety
    for i in range(len(questions)):
        active_class = "node-active" if i == idx else ""
        with cols[i % 10]:
            st.markdown(f'<div class="pagination-node {active_class}">{i+1}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with f_col2:
    # Neural Next Button
    st.markdown('<div class="neural-btn" style="text-align: right;">', unsafe_allow_html=True)
    next_label = "Next Node →" if idx < len(questions) - 1 else "Finish Session ✓"
    if st.button(next_label, use_container_width=True, key="next_btn"):
        if idx < len(questions) - 1:
            st.session_state['current_idx'] += 1
            st.session_state['q_start_time'] = time.time()
            st.rerun()
        else:
            st.switch_page("pages/results.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Auto-timeout
if res is None and remaining == 0:
    st.session_state['feedback'][idx] = "Timeout"
    st.rerun()

if res is None and remaining > 0:
    time.sleep(1)
    st.rerun()

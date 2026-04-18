import streamlit as st
import json
import pandas as pd
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="Admin Node", page_icon="⚙️", layout="wide")

# Internal Initialization
set_page_style()

if 'admin_logged_in' not in st.session_state:
    st.session_state['admin_logged_in'] = False

st.title("⚙️ ADMIN OVERRIDE")

# PIN Protection
if 'admin_auth' not in st.session_state:
    st.session_state['admin_auth'] = False

if not st.session_state['admin_auth']:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.write("### Identity Verification Required")
    pin = st.text_input("Enter Access PIN:", type="password", key="admin_pin_input")
    if st.button("AUTHENTICATE"):
        if pin == "1234":
            st.session_state['admin_auth'] = True
            st.rerun()
        else:
            st.error("Access Denied. Identity Not Verified.")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    tab1, tab2 = st.tabs(["📂 QUESTION BANK", "📤 UPLOAD DATA"])
    
    # Tab 1: Question Bank Management
    with tab1:
        st.subheader("Central Question Index")
        try:
            with open("data/question_bank.json", "r") as f:
                questions = json.load(f)
            
            df_q = pd.DataFrame(questions)
            st.dataframe(df_q, use_container_width=True)
            
            st.divider()
            st.subheader("Add New Research Portal")
            with st.form("add_question_v3"):
                q_text = st.text_input("Question Text")
                q_cat = st.selectbox("Category", ["Science", "Math", "History", "General Knowledge"])
                q_diff = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
                c1, c2 = st.columns(2)
                o1 = c1.text_input("Option 1")
                o2 = c2.text_input("Option 2")
                o3 = c1.text_input("Option 3")
                o4 = c2.text_input("Option 4")
                ans = st.selectbox("Correct Answer", [o1, o2, o3, o4])
                
                st.markdown('<div id="green-marker"></div>', unsafe_allow_html=True)
                if st.form_submit_button("COMMIT TO STORAGE"):
                    new_q = {
                        "category": q_cat, "difficulty": q_diff, 
                        "question": q_text, "options": [o1, o2, o3, o4], "answer": ans
                    }
                    questions.append(new_q)
                    with open("data/question_bank.json", "w") as f:
                        json.dump(questions, f, indent=4)
                    st.success("New portal committed to neural storage.")
                    st.rerun()
        except Exception as e:
            st.error(f"Storage Sync Error: {e}")

    # Tab 2: File Upload
    with tab2:
        st.subheader("Sub-routine: Bulk Data Ingestion")
        uploaded_file = st.file_uploader("Upload CSV or JSON portal pack", type=['csv', 'json'])
        if uploaded_file:
            if uploaded_file.name.endswith('.json'):
                new_data = json.load(uploaded_file)
            else:
                new_data = pd.read_csv(uploaded_file).to_dict(orient='records')
            
            st.write("Ingestion Preview:")
            st.dataframe(new_data)
            
            st.markdown('<div id="green-marker"></div>', unsafe_allow_html=True)
            if st.button("SYNC DATASETS"):
                with open("data/question_bank.json", "r") as f:
                    current_data = json.load(f)
                current_data.extend(new_data)
                with open("data/question_bank.json", "w") as f:
                    json.dump(current_data, f, indent=4)
                st.success(f"Success: {len(new_data)} portals merged.")

    st.markdown('<div id="red-marker"></div>', unsafe_allow_html=True)
    if st.button("LOGOUT OF NODE"):
        st.session_state['admin_auth'] = False
        st.switch_page("app.py")

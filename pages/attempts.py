import streamlit as st
import pandas as pd
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="Attempt History | QuizForge", page_icon="📜", layout="wide")
set_page_style()

st.title("📜 NEURAL LOGS")
st.markdown("### SYSTEM HISTORY & PERFORMANCE TRACKING")

try:
    df = pd.read_csv("data/leaderboard.csv")
    if df.empty:
        st.info("No neural logs found. Initialize your first session to begin tracking.")
    else:
        # Schema Harmonization (Handle legacy and new columns)
        if 'Date' in df.columns:
            df['Timestamp'] = df['Timestamp'].fillna(df['Date'])
        if 'Category' in df.columns:
            df['Topic'] = df['Topic'].fillna(df['Category'])
        if 'Percentage' in df.columns:
            # Ensure Accuracy is a string with % for consistency
            df['Accuracy'] = df['Accuracy'].fillna(df['Percentage'].apply(lambda x: f"{x:.1f}%" if pd.notnull(x) else "0.0%"))
        if 'Name' in df.columns:
            df['User'] = df['User'].fillna(df['Name'])

        # Final cleanup and sort
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='mixed', errors='coerce')
        df = df.sort_values(by='Timestamp', ascending=False)
        
        for index, row in df.iterrows():
            # Skip rows with no valid timestamp
            if pd.isnull(row['Timestamp']): continue
            
            # Formatting Topic
            topic = str(row['Topic']).upper() if pd.notnull(row['Topic']) else "UNKNOWN"
            user = str(row['User']) if pd.notnull(row['User']) else "ANONYMOUS"
            accuracy = str(row['Accuracy']) if pd.notnull(row['Accuracy']) else "0.0%"
            st.markdown(f"""
            <div class="history-card" style="border-left: 4px solid var(--accent);">
                <div>
                    <div style="font-family: 'Orbitron'; color: var(--accent); font-size: 1.1rem; letter-spacing: 1px;">{topic} ASSESSMENT</div>
                    <div style="color: rgba(255,255,255,0.5); font-size: 0.8rem; font-family: Inter;">{row['Timestamp'].strftime('%d %b %Y | %H:%M:%S')}</div>
                    <div style="margin-top: 8px; font-family: Inter;">Identity: <span style="color: white; font-weight: 600;">{user}</span></div>
                </div>
                <div style="text-align: right;">
                    <div style="font-family: 'Orbitron'; font-size: 1.8rem; color: #FFFFFF; font-weight: bold;">{accuracy}</div>
                    <div style="font-size: 0.7rem; color: rgba(255,255,255,0.4); letter-spacing: 1px;">PRECISION</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

except Exception as e:
    st.error(f"Portal Error: Unable to retrieve neural history logs. Details: {e}")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div id="red-marker"></div>', unsafe_allow_html=True)
if st.button("← RETURN TO HUB"):
    st.switch_page("pages/quizz.py")

import streamlit as st
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="NexBot Neural | QuizForge", page_icon="🤖", layout="wide")
set_page_style()

# Embed the 3D Robo Landing Page
try:
    with open("index.html", "r") as f: html_content = f.read()
    with open("style.css", "r") as f: css_content = f.read()
    
    # Inject CSS
    full_html = html_content.replace('<link rel="stylesheet" href="style.css">', f'<style>{css_content}</style>')
    
    # Redirection Fix: Transition to the dedicated /quizz portal
    full_html = full_html.replace('href="http://localhost:8502"', 'href="/quizz" target="_self"')
    full_html = full_html.replace('href="/?view=portal"', 'href="/quizz" target="_self"')
    
    st.components.v1.html(full_html, height=1000, scrolling=False)
    st.markdown("""
        <style>
            iframe { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; border: none; z-index: 9999; } 
            [data-testid='stHeader'] { display: none !important; }
            [data-testid="stSidebar"] { display: none !important; }
        </style>
    """, unsafe_allow_html=True)
    st.stop()
except Exception as e:
    st.error(f"Landing Portal Error: {e}")

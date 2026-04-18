import streamlit as st
import pandas as pd
import plotly.express as px
from utils.ui_components import set_page_style

# Page Setup
st.set_page_config(page_title="Global Leaderboard", page_icon="🏆", layout="wide")
set_page_style()

st.title("🏆 GLOBAL RANKINGS")

try:
    df = pd.read_csv("data/leaderboard.csv")
    if df.empty:
        st.info("Neural network is currently empty. No data recorded.")
    else:
        # Harmonize schema
        if 'Category' in df.columns:
            df['Topic'] = df['Topic'].fillna(df['Category'])
        if 'Percentage' in df.columns:
            df['Accuracy'] = df['Accuracy'].fillna(df['Percentage'].apply(lambda x: f"{x:.1f}%" if pd.notnull(x) else "0.0%"))
        if 'Name' in df.columns:
            df['User'] = df['User'].fillna(df['Name'])

        # Filter by Topic
        st.subheader("Leaderboard Analysis")
        topics = df['Topic'].dropna().unique()
        if len(topics) > 0:
            top_filter = st.multiselect("Filter Nodes:", topics, default=topics)
            filtered_df = df[df['Topic'].isin(top_filter)]
        else:
            filtered_df = df
        
        # Sort and clean
        filtered_df = filtered_df.sort_values(by=['Accuracy'], ascending=False)
        
        display_df = filtered_df[['User', 'Topic', 'Accuracy', 'Timestamp']].head(20).reset_index(drop=True)
        display_df.index += 1
        
        st.dataframe(display_df, use_container_width=True)

except Exception as e:
    st.error(f"Portal Error: {e}")

st.markdown('<div id="red-marker"></div>', unsafe_allow_html=True)
if st.button("RETURN TO HUB"):
    st.switch_page("pages/quizz.py")

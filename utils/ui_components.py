import streamlit as st

def set_page_style():
    """Restores high-contrast Neural Balance and fixes the Ultra-White regression."""
    # ANTI-FLICKER + GLOBAL DARK FORCE
    st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], .stApp, [data-testid="stSidebar"], .main {
            background-color: #05050A !important;
            color: #FFFFFF !important;
        }
        [data-testid="stHeader"], [data-testid="stDecoration"] {
            display: none !important;
            height: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');

        :root {
            --bg-color: #05050A;
            --accent: #10B981; /* Emerald Green */
            --red-accent: #EF4444; /* Crimson Red */
            --neural-timer: #06B6D4;
            --neural-violet: #8B5CF6;
        }

        /* WIDGET LABELS: Clear white visibility */
        label[data-testid="stWidgetLabel"], .stMarkdown p, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            color: #FFFFFF !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* INPUT FIELDS: Deep black background with white text */
        input, textarea, select, div[data-baseweb="input"], [data-testid="stSelectbox"] div {
            background-color: #0A0A0F !important;
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 8px !important;
        }

        /* DYNAMIC BUTTONS: Default Dark Card Look (Image 2 Sync) */
        .stButton>button {
            background: rgba(255, 255, 255, 0.03) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
            text-transform: none !important;
            text-align: left !important;
            padding: 15px 25px !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            border-color: var(--accent) !important;
            background: rgba(16, 185, 129, 0.05) !important;
        }

        /* NEURAL PRIMARY BUTTONS (Image 2 - Next) */
        /* GREEN NEURAL BUTTON (Marker-based) */
        div.element-container:has(#green-marker) + div.element-container .stButton > button,
        div.element-container:has(#green-marker) + div.element-container .stFormSubmitButton > button {
            background: linear-gradient(135deg, #10B981, #065F46) !important;
            color: #FFFFFF !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-family: 'Orbitron' !important;
            border: none !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }
        
        div.element-container:has(#green-marker) + div.element-container .stButton > button:hover,
        div.element-container:has(#green-marker) + div.element-container .stFormSubmitButton > button:hover {
            background: linear-gradient(135deg, #059669, #064E3B) !important;
            box-shadow: 0 0 15px rgba(16, 185, 129, 0.4) !important;
            transform: scale(1.02);
        }

        .neural-btn > div > button {
            background: linear-gradient(135deg, var(--neural-violet), #4F46E5) !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-family: 'Orbitron' !important;
            border: none !important;
        }

        /* RED NEURAL BUTTON (Marker-based) */
        div.element-container:has(#red-marker) + div.element-container .stButton > button {
            background: linear-gradient(135deg, #EF4444, #991B1B) !important;
            color: #FFFFFF !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-family: 'Orbitron' !important;
            border: none !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }
        
        div.element-container:has(#red-marker) + div.element-container .stButton > button:hover {
            background: linear-gradient(135deg, #FF5555, #B91C1C) !important;
            box-shadow: 0 0 15px rgba(239, 68, 68, 0.4) !important;
            transform: scale(1.02);
        }

        /* VIOLET NEURAL BUTTON (Marker-based for Landing Actions) */
        div.element-container:has(#violet-marker) + div.element-container .stButton > button {
            background: linear-gradient(135deg, #6366F1, #4F46E5) !important; /* Indigo to Violet */
            color: #FFFFFF !important;
            text-align: center !important;
            text-transform: uppercase !important;
            font-family: 'Orbitron' !important;
            border: none !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(79, 70, 229, 0.2) !important;
        }
        
        div.element-container:has(#violet-marker) + div.element-container .stButton > button:hover {
            background: linear-gradient(135deg, #818CF8, #4F46E5) !important;
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.5) !important;
            transform: scale(1.02);
        }

        /* HUB CARDS: Clean Glass Containers */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: rgba(255, 255, 255, 0.02) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 15px !important;
        }

        /* OPTION CARDS (Quiz) */
        .quiz-option-card {
            background: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        
        .letter-marker {
            background: rgba(255, 255, 255, 0.1);
            color: #FFFFFF;
            width: 35px;
            height: 35px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 6px;
            font-weight: bold;
            margin-right: 15px;
        }

        .correct-opt { border-color: var(--accent) !important; background: rgba(16, 185, 129, 0.1) !important; }
        .wrong-opt { border-color: var(--red-accent) !important; background: rgba(239, 68, 68, 0.1) !important; }

        /* SIDEBAR SYNC: Pure White Text */
        [data-testid="stSidebar"] {
            background-color: #05050A !important;
            border-right: 1px solid rgba(255,255,255,0.05);
        }
        
        [data-testid="stSidebarNav"] a span {
            color: #FFFFFF !important;
            font-family: 'Orbitron', sans-serif !important;
            font-weight: 400 !important;
            letter-spacing: 1px;
        }

        /* Active Sidebar Indicator */
        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background-color: rgba(16, 185, 129, 0.1) !important;
            border-left: 3px solid var(--accent) !important;
        }

        /* PILLS */
        .quiz-pill {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-family: 'Inter', sans-serif;
            border: 1px solid rgba(255,255,255,0.1);
        }
        .pill-score { color: #F59E0B; background: rgba(245, 158, 11, 0.1); }
        .pill-correct { color: #10B981; background: rgba(16, 185, 129, 0.1); }
        .pill-wrong { color: #EF4444; background: rgba(239, 68, 68, 0.1); }

        /* TOPIC CARDS (Student Hub) */
        .topic-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            transition: all 0.3s ease;
            margin-bottom: 20px;
        }
        
        .topic-selected {
            border-color: var(--red-accent) !important;
            background: rgba(239, 68, 68, 0.05) !important;
            box-shadow: 0 0 20px rgba(239, 68, 68, 0.1);
        }

        /* CIRCULAR PROGRESS (Results) */
        .score-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 20px 0;
        }
        .score-circle {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            background: conic-gradient(var(--neural-violet) var(--percentage), rgba(255,255,255,0.05) 0);
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        .score-circle::before {
            content: "";
            position: absolute;
            width: 155px;
            height: 155px;
            background: #05050A;
            border-radius: 50%;
        }
        .score-inner {
            z-index: 10;
            text-align: center;
        }
        .score-value {
            font-family: 'Orbitron', sans-serif;
            font-size: 3rem;
            font-weight: bold;
            color: #FFFFFF;
            line-height: 1;
        }
        .score-label {
            font-family: 'Inter', sans-serif;
            font-size: 0.8rem;
            color: var(--neural-violet);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-top: 5px;
        }

        /* 2x2 STAT GRID (Results) */
        .result-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .stat-val {
            font-family: 'Orbitron', sans-serif;
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .stat-label {
            font-size: 0.7rem;
            color: rgba(255,255,255,0.5);
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        /* HISTORY CARDS (Neural Logs) */
        .history-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: transform 0.2s ease;
        }
        .history-card:hover {
            transform: translateX(10px);
            background: rgba(255, 255, 255, 0.04);
            border-color: rgba(255, 255, 255, 0.1);
        }

        /* PAGINATION NODES (Quiz Footer) */
        .pagination-container {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }
        .pagination-node {
            width: 35px;
            height: 35px;
            border-radius: 8px;
            background: var(--neural-violet);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-family: 'Orbitron', sans-serif;
            font-size: 0.9rem;
            opacity: 0.5;
            transition: all 0.3s ease;
        }
        .node-active {
            opacity: 1;
            box-shadow: 0 0 15px var(--neural-violet);
            border: 2px solid white;
        }

        /* HIDE INTERNAL PAGES */
        [data-testid="stSidebarNav"] li:has(a[href*="session"]), 
        [data-testid="stSidebarNav"] li:has(a[href*="results"]),
        [data-testid="stSidebarNav"] li:has(a[href*="student_hub"]) {
            display: none !important;
        }
    </style>
    """, unsafe_allow_html=True)

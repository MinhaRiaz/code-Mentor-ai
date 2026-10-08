import os
import streamlit as st

from crewai import Crew, Process
from agents import create_agents
from tasks import create_tasks

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CodeMentor AI",
    page_icon="https://cdn-icons-png.flaticon.com/512/4712/4712035.png",
    layout="centered" 
)

# -----------------------------
# Initialize Session State
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Custom CSS for Vibrant UI
# -----------------------------
st.markdown("""
    <style>
    :root {
        --brand-gradient: linear-gradient(45deg, #ff00cc, #3333ff, #00d2ff);
        --brand-color: #3333ff;
    }
    
    /* Modern Mesh Background */
    .stApp {
        background-color: #0b0f19;
        background-image: 
            radial-gradient(at 18% 15%, rgba(99, 102, 241, 0.25) 0px, transparent 50%),
            radial-gradient(at 80% 20%, rgba(168, 85, 247, 0.2) 0px, transparent 50%),
            radial-gradient(at 40% 80%, rgba(14, 165, 233, 0.2) 0px, transparent 50%);
        background-attachment: fixed;
    }
    
    /* Adjust Text Colors for Dark Theme */
    .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp label, .stApp span {
        color: #e2e8f0 !important;
    }

    /* Glowing Title */
    .title-gradient {
        background: var(--brand-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 5px;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #94a3b8 !important; /* Lighter subtitle color for dark bg */
        margin-bottom: 2rem;
        letter-spacing: 1px;
        font-weight: 600;
    }
    
    /* Input Styling */
    .stTextArea textarea, .stTextInput input {
        border-radius: 12px;
        border: 2px solid #334155;
        background-color: rgba(30, 41, 59, 0.7); /* Slightly transparent dark inputs */
        color: #f8fafc;
        transition: border-color 0.3s, background-color 0.3s;
    }
    .stTextArea textarea:focus, .stTextInput input:focus {
        border-color: var(--brand-color);
        background-color: rgba(30, 41, 59, 1);
        box-shadow: 0 0 10px rgba(51, 51, 255, 0.4);
    }
    
    /* Selectbox Styling */
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
        border: 2px solid #334155;
        background-color: rgba(30, 41, 59, 0.7);
    }
    
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: transparent; /* Fix inner select bg */
        color: #f8fafc;
    }

    /* Gradient Material Icons */
    .material-symbols-rounded {
        background: var(--brand-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }

    /* Button Icon Exception */
    div.stButton > button .material-symbols-rounded {
        background: none;
        -webkit-text-fill-color: white;
        color: white;
    }
    
    /* Main Action Button */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        font-weight: 800;
        font-size: 18px;
        background: var(--brand-gradient);
        color: white !important;
        border: none;
        box-shadow: 0 4px 15px rgba(51, 51, 255, 0.4);

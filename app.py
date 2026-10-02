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
    page_icon="💻",
    layout="centered" # Centered for a clean, modern web app feel
)

# -----------------------------
# Custom CSS for Modern UI Polish
# -----------------------------
st.markdown("""
    <style>
    .stTextArea textarea {
        border-radius: 12px;
        border: 1px solid #e2e8f0;
    }
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
    }
    .stTextInput input {
        border-radius: 12px;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 52px;
        font-weight: 600;
        font-size: 16px;
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
        color: white;
        border: none;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    }
    .hero-text {
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Get API Key & Set Environment
# -----------------------------
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error(":material/key_off: **GEMINI_API_KEY** is not configured in Streamlit Secrets.")
    st.stop()
os.environ["GEMINI_API_KEY"] = api_key

# -----------------------------
# Sidebar: Information & Guide
# -----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=75)
    st.title("CodeMentor AI")
    st.markdown("Your personal, AI-powered programming mentor.")
    st.divider()
    st.markdown("### :material/schema: How it works")
    st.markdown("""
    1. **:material/code: Coding Expert** writes clear syntax examples.
    2. **:material/map: Learning Planner** builds a phased roadmap.
    3. **:material/rate_review: Reviewer** polishes it into a perfect guide.
    """)
    st.divider()
    st.info(":material/workspace_premium: Built for **PakAngel’s Generative AI Hackathon**")

# -----------------------------
# Main UI: Hero Section
# -----------------------------
st.markdown("<div class='hero-text'>", unsafe_allow_html=True)
st.title(":material/terminal: CodeMentor AI")
st.markdown("#### Generate a personalized coding roadmap and syntax guide in seconds.")
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Main UI: Input Cards
# -----------------------------
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        language = st.text_input(
            ":material/code: Programming Language",
            placeholder="e.g. Python, Flutter, JavaScript"
        )
        
    with col2:
        level = st.selectbox(
            ":material/leaderboard: Experience Level",
            ["Complete Beginner", "Beginner", "Intermediate"]
        )

    question = st.text_area(
        ":material/chat: What specific concepts do you want to learn?",
        placeholder="Example: I want to learn Python from zero. Show me variables and loops.",
        height=120
    )

# -----------------------------
# Run Agents
# -----------------------------
if st.button(":material/rocket_launch: Generate My Learning Roadmap", type="primary"):

    if not language.strip():
        st.warning(":material/warning: Please enter a programming language to continue.")
        st.stop()

    if not question.strip():
        st.warning(":material/warning: Please enter your learning question to continue.")
        st.stop()

    inputs = {
        "language": language,
        "level": level,
        "question": question
    }

    try:
        st.divider()
        # Dynamic Hackathon Demo UI with Material Icons
        with st.status(":material/smart_toy: **Initializing CodeMentor Agents...**", expanded=True) as status:
            
            st.write(":material/check_circle: Loading learner profile and setting up environment...")
            (coding_agent, learning_agent, reviewer_agent) = create_agents(api_key)
            (coding_task, roadmap_task, review_task) = create_tasks(coding_agent, learning_agent, reviewer_agent)

            st.write(":material/verified: Coding Expert, Learning Planner, and Reviewer are online.")
            
            crew = Crew(
                agents=[coding_agent, learning_agent, reviewer_agent],
                tasks=[coding_task, roadmap_task, review_task],
                process=Process.sequential,
                verbose=False
            )

            st.write(":material/hourglass_top: Agents are drafting your custom curriculum (approx. 15-20 seconds)...")
            result = crew.kickoff(inputs=inputs)
            
            status.update(label=":material/auto_awesome: Learning Roadmap Complete!", state="complete", expanded=False)

        # -------------------------
        # Display Final Result
        # -------------------------
        with st.container():
            st.markdown("### :material/school: Your Personalized Guide")
            output_text = result.raw if hasattr(result, "raw") else str(result)
            
            st.info(":material/tips_and_updates: Here is the combined output from your AI mentors:")
            st.markdown(output_text)

    except Exception as e:
        error_msg = str(e)
        if "503" in error_msg or "high demand" in error_msg or "UNAVAILABLE" in error_msg:
            st.warning(":material/traffic: Google's AI servers are currently experiencing high traffic.")
            if st.button(":material/refresh: Retry Request"):
                st.rerun()
        else:
            st.error(":material/error: Something went wrong.")
            st.code(error_msg)

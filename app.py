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
# Custom CSS for Vibrant, Colorful UI
# -----------------------------
st.markdown("""
    <style>
    /* Glowing Title Gradient */
    .title-gradient {
        background: linear-gradient(to right, #ff00cc, #3333ff, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 10px;
    }
    .hero-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    /* Vibrant Sunset Action Button */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        font-weight: 800;
        font-size: 18px;
        background: linear-gradient(45deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(221, 36, 118, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(221, 36, 118, 0.6);
        color: white;
    }

    /* Soft Inputs with Colorful Focus Rings */
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #f0f0f0;
        transition: border-color 0.3s;
    }
    .stTextArea textarea:focus {
        border-color: #DD2476;
        box-shadow: 0 0 10px rgba(221, 36, 118, 0.2);
    }
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
        border: 2px solid #f0f0f0;
    }
    
    /* Output Card Polish */
    .output-header {
        color: #DD2476;
        font-weight: 800;
        border-bottom: 2px solid #DD2476;
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
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
# Sidebar: Colorful Information Guide
# -----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=90)
    st.markdown("## CodeMentor AI")
    st.markdown("Your personal, AI-powered programming mentor.")
    st.divider()
    st.markdown("### :material/schema: The AI Crew")
    st.markdown("""
    🟢 **Coding Expert:** Writes your syntax.\n
    🔵 **Learning Planner:** Builds the roadmap.\n
    🟣 **Reviewer:** Polishes the final guide.
    """)
    st.divider()

# -----------------------------
# Main UI: Hero Section
# -----------------------------
st.markdown("<h1 class='title-gradient'>CodeMentor AI</h1>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Generate a highly personalized coding roadmap and syntax guide in seconds.</div>", unsafe_allow_html=True)

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

            st.write(":material/hourglass_top: Agents are collaborating to build your curriculum...")
            result = crew.kickoff(inputs=inputs)
            
            status.update(label=":material/auto_awesome: Learning Roadmap Complete!", state="complete", expanded=False)

        # -------------------------
        # Display Final Result
        # -------------------------
        st.markdown("<h2 class='output-header'>🎓 Your Personalized Guide</h2>", unsafe_allow_html=True)
        
        output_text = result.raw if hasattr(result, "raw") else str(result)
        
        st.info(":material/tips_and_updates: Here is the masterclass combined from your three AI mentors:")
        
        # Displaying the main AI output
        st.markdown(output_text)

    except Exception as e:
        error_msg = str(e)
        if "503" in error_msg or "high demand" in error_msg or "UNAVAILABLE" in error_msg:
            st.warning(":material/traffic: Google's AI servers are currently experiencing high traffic. Please try again.")
            if st.button(":material/refresh: Retry Request"):
                st.rerun()
        else:
            st.error(":material/error: Something went wrong.")
            st.code(error_msg)

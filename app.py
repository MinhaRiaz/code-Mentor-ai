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
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(51, 51, 255, 0.6);
        color: white !important;
    }

    /* Output Section Styling */
    .output-header {
        background: var(--brand-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        border-bottom: 2px solid var(--brand-color);
        padding-bottom: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    .sidebar-logo {
        text-align: center;
        font-size: 5rem;
        margin-bottom: -20px;
    }
    
    /* Sidebar Styling to match theme */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8);
        border-right: 1px solid rgba(255,255,255,0.05);
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
# Helper Function to Run Agents
# -----------------------------
def run_codementor_agents(inputs_dict):
    with st.status(":material/smart_toy: **Initializing CodeMentor Agents...**", expanded=True) as status:
        st.write(":material/check_circle: Loading environment & task parameters...")
        (coding_agent, learning_agent, reviewer_agent) = create_agents(api_key)
        (coding_task, roadmap_task, review_task) = create_tasks(coding_agent, learning_agent, reviewer_agent)

        st.write(":material/verified: Coding Expert, Learning Planner, and Reviewer are online.")
        
        crew = Crew(
            agents=[coding_agent, learning_agent, reviewer_agent],
            tasks=[coding_task, roadmap_task, review_task],
            process=Process.sequential,
            verbose=False
        )

        st.write(":material/hourglass_top: Agents are collaborating to generate your result...")
        result = crew.kickoff(inputs=inputs_dict)
        
        status.update(label=":material/auto_awesome: Result Ready!", state="complete", expanded=False)
        
        return result.raw if hasattr(result, "raw") else str(result)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=90)
    st.markdown("## CodeMentor AI")
    st.markdown("Your personal, AI-powered programming mentor.")
    st.divider()
    st.markdown("### :material/schema: The AI Crew")
    st.markdown("""
    🟢 **Coding Expert:** Writes & reviews code.\n
    🔵 **Learning Planner:** Builds roadmaps.\n
    🟣 **Reviewer:** Polishes final output.
    """)
    if st.button("🗑️ Clear History"):
        st.session_state.chat_history = []
        st.rerun()
    st.divider()

# -----------------------------
# Main UI: Hero Section
# -----------------------------
st.markdown("<h1 class='title-gradient'>CodeMentor AI</h1>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>WHAT ARE WE BUILDING?</div>", unsafe_allow_html=True)

# -----------------------------
# Main UI: Input Cards (Hides after first submission)
# -----------------------------
if len(st.session_state.chat_history) == 0:
    with st.container():
        # 1. Action Type Dropdown
        task_type = st.selectbox(
            ":material/help: What would you like to focus on?",
            ["Generate code", "Learning roadmap", "Explain a concept", "Review my code"]
        )

        col1, col2 = st.columns(2)
        
        with col1:
            # 2. Programming Language Dropdown
            language = st.selectbox(
                ":material/code: Programming language",
                ["Python", "JavaScript", "Java", "C++", "C#", "HTML/CSS", "SQL", "Other"]
            )
            
        with col2:
            # 3. Experience Level Dropdown
            level = st.selectbox(
                ":material/leaderboard: Experience level",
                ["Beginner", "Intermediate", "Advanced"]
            )

        # 4. Conditional Learning Time Slider
        learning_time = 30
        if task_type == "Learning roadmap":
            learning_time = st.slider(
                ":material/schedule: Learning time (hours/days allocated for roadmap)",
                min_value=5, max_value=100, value=30, step=5
            )

        # 5. Question / Code Prompt Text Area
        question = st.text_area(
            ":material/chat: Describe your goal or paste your code",
            placeholder="Example: Give me loops code or explain how functions work...",
            height=120
        )

    # -----------------------------
    # Initial Run Button
    # -----------------------------
    if st.button(":material/auto_awesome: Generate", type="primary"):
        if not question.strip():
            st.warning(":material/warning: Please describe your goal or paste your code to continue.")
            st.stop()

        inputs = {
            "task_type": task_type,
            "language": language,
            "level": level,
            "learning_time": str(learning_time),
            "question": question
        }

        try:
            st.divider()
            output_text = run_codementor_agents(inputs)
            
            # Save inputs and outputs to history
            st.session_state.chat_history.append({"role": "user", "content": question})
            st.session_state.chat_history.append({"role": "ai", "content": output_text, "context": inputs})
            st.rerun()

        except Exception as e:
            error_msg = str(e)
            if "503" in error_msg or "high demand" in error_msg or "UNAVAILABLE" in error_msg:
                st.warning(":material/traffic: Google's AI servers are currently experiencing high traffic. Please try again.")
            else:
                st.error(":material/error: Something went wrong.")
                st.code(error_msg)

# -----------------------------
# Display History & Follow-Up Bar
# -----------------------------
if len(st.session_state.chat_history) > 0:
    st.markdown("<h2 class='output-header'>🎓 Your Mentorship Session</h2>", unsafe_allow_html=True)
    
    # Render all past messages
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant"):
                st.info(message["content"])

    # Bottom sticky chat bar for follow-ups
    follow_up = st.chat_input("Ask a follow-up question or generate more code...")
    
    if follow_up:
        # Save new user request
        st.session_state.chat_history.append({"role": "user", "content": follow_up})
        
        # Inherit settings from the very first AI message context
        first_ai_msg = next((msg for msg in st.session_state.chat_history if msg["role"] == "ai"), None)
        
        new_inputs = {
            "task_type": "Follow-up Question",
            "language": first_ai_msg["context"]["language"] if first_ai_msg else "Python",
            "level": first_ai_msg["context"]["level"] if first_ai_msg else "Intermediate",
            "learning_time": first_ai_msg["context"]["learning_time"] if first_ai_msg else "30",
            "question": f"Previous context exists. User's new follow-up request: {follow_up}"
        }

        try:
            output_text = run_codementor_agents(new_inputs)
            st.session_state.chat_history.append({"role": "ai", "content": output_text, "context": new_inputs})
            st.rerun()
            
        except Exception as e:
            st.error(f":material/error: Something went wrong. Error: {str(e)}")

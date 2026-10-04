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
    page_icon="👨‍💻",
    layout="centered" 
)

# -----------------------------
# Custom CSS for UI Polish
# -----------------------------
st.markdown("""
    <style>
    :root {
        --brand-gradient: linear-gradient(45deg, #ff00cc, #3333ff, #00d2ff);
        --brand-color: #3333ff;
    }

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
        color: #888899;
        margin-bottom: 2rem;
    }

    /* Input Styling */
    .stTextArea textarea, .stTextInput input {
        border-radius: 12px;
        border: 2px solid #2b2b36;
    }
    
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 12px;
    }
    
    /* Main Action Button */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        font-weight: 800;
        font-size: 18px;
        background: var(--brand-gradient);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(51, 51, 255, 0.4);
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(51, 51, 255, 0.6);
        color: white;
    }

    /* Output Card Polish */
    .output-header {
        color: var(--brand-color);
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
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("<div class='sidebar-logo'><span class='material-symbols-rounded' style='font-size: 80px;'>hub</span></div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>CodeMentor AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Your personal, AI-powered programming mentor.</p>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### :material/schema: The AI Crew")
    st.markdown("""
    🟢 **Coding Expert:** Writes & reviews code.\n
    🔵 **Learning Planner:** Builds roadmaps.\n
    🟣 **Reviewer:** Polishes final output.
    """)
    st.divider()
    st.success(":material/workspace_premium: **PakAngel’s Hackathon Build**")

# -----------------------------
# Main Hero Section
# -----------------------------
st.markdown("<h1 class='title-gradient'>CodeMentor AI</h1>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>01 / TELL US WHAT YOU WANT TO DO</div>", unsafe_allow_html=True)

# -----------------------------
# Form Inputs
# -----------------------------
with st.container():
    # 1. Action Type Selection
    task_type = st.selectbox(
        ":material/help: What do you need help with?",
        ["Generate code", "Learning roadmap", "Explain a concept", "Review my code"]
    )

    col1, col2 = st.columns(2)
    
    with col1:
        # 2. Programming Language Selection
        language = st.selectbox(
            ":material/code: Programming language",
            ["Python", "JavaScript", "Java", "C++", "C#", "HTML/CSS", "SQL", "Other"]
        )
        
    with col2:
        # 3. Experience Level Selection
        level = st.selectbox(
            ":material/leaderboard: Your experience level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    # 4. Conditional Learning Time Slider (shown for roadmaps)
    learning_time = 30
    if task_type == "Learning roadmap":
        learning_time = st.slider(
            ":material/schedule: Learning time (hours/days allocated for roadmap)",
            min_value=5, max_value=100, value=30, step=5
        )

    # 5. User Goal / Code Input
    question = st.text_area(
        ":material/chat: Describe your goal or paste your code",
        placeholder="Example: Give me loops code or explain how variables work...",
        height=120
    )

# -----------------------------
# Run Agents
# -----------------------------
if st.button("✨ Build my result", type="primary"):

    if not question.strip():
        st.warning(":material/warning: Please describe your goal or paste code to continue.")
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
        with st.status(":material/smart_toy: **Initializing CodeMentor Agents...**", expanded=True) as status:
            
            st.write(":material/check_circle: Setting up environment & context...")
            (coding_agent, learning_agent, reviewer_agent) = create_agents(api_key)
            (coding_task, roadmap_task, review_task) = create_tasks(coding_agent, learning_agent, reviewer_agent)

            st.write(":material/verified: Agents are online and collaborating...")
            
            crew = Crew(
                agents=[coding_agent, learning_agent, reviewer_agent],
                tasks=[coding_task, roadmap_task, review_task],
                process=Process.sequential,
                verbose=False
            )

            st.write(":material/hourglass_top: Generating your personalized output...")
            result = crew.kickoff(inputs=inputs)
            
            status.update(label=":material/auto_awesome: Result Ready!", state="complete", expanded=False)

        # -------------------------
        # Display Output & Download
        # -------------------------
        st.markdown("<h2 class='output-header'>🎓 Result</h2>", unsafe_allow_html=True)
        
        output_text = result.raw if hasattr(result, "raw") else str(result)
        st.markdown(output_text)

        st.divider()
        
        # 6. Download as Markdown Feature
        st.download_button(
            label="⬇️ Download result as Markdown",
            data=output_text,
            file_name=f"{language}_{task_type.replace(' ', '_')}.md",
            mime="text/markdown",
            use_container_width=True
        )

    except Exception as e:
        error_msg = str(e)
        if "503" in error_msg or "high demand" in error_msg or "UNAVAILABLE" in error_msg:
            st.warning(":material/traffic: Google's AI servers are currently experiencing high traffic. Please try again.")
            if st.button(":material/refresh: Retry Request"):
                st.rerun()
        else:
            st.error(":material/error: Something went wrong.")
            st.code(error_msg)

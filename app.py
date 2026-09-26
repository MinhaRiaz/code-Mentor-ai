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
    layout="wide"
)


# -----------------------------
# App Title
# -----------------------------
st.title("👨‍💻 CodeMentor AI")

st.caption(
    "A beginner-friendly Multi-Agent Coding and Learning Assistant"
)


# -----------------------------
# Get API Key & Set Environment Variable
# -----------------------------
# Retrieve the Gemini API key from Streamlit secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY is not configured in Streamlit Secrets.")
    st.stop()

# Inject into OS environment so LiteLLM and CrewAI can read it automatically
os.environ["GEMINI_API_KEY"] = api_key


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("👩‍💻 Learner Profile")

    level = st.selectbox(
        "Experience Level",
        [
            "Complete Beginner",
            "Beginner",
            "Intermediate"
        ]
    )

    language = st.text_input(
        "Programming Language",
        placeholder="e.g. Python, Flutter, Java"
    )


# -----------------------------
# User Question
# -----------------------------
question = st.text_area(
    "What do you want to learn?",
    placeholder=(
        "Example: I want to learn Python from zero. "
        "Explain the basics and give me a roadmap."
    ),
    height=180
)


# -----------------------------
# Run Agents
# -----------------------------
if st.button("Ask CodeMentor AI", type="primary"):

    if not language.strip():
        st.warning("Please enter a programming language.")
        st.stop()

    if not question.strip():
        st.warning("Please enter your learning question.")
        st.stop()

    # -------------------------
    # User Information Inputs
    # -------------------------
    inputs = {
        "language": language,
        "level": level,
        "question": question
    }

    try:

        with st.spinner(
            "🤖 The three AI agents are working together..."
        ):

            # ---------------------
            # Create Agents
            # ---------------------
            (
                coding_agent,
                learning_agent,
                reviewer_agent
            ) = create_agents(api_key)


            # ---------------------
            # Create Tasks
            # ---------------------
            (
                coding_task,
                roadmap_task,
                review_task
            ) = create_tasks(
                coding_agent,
                learning_agent,
                reviewer_agent
            )


            # ---------------------
            # Create Crew
            # ---------------------
            crew = Crew(
                agents=[
                    coding_agent,
                    learning_agent,
                    reviewer_agent
                ],
                tasks=[
                    coding_task,
                    roadmap_task,
                    review_task
                ],
                process=Process.sequential,
                verbose=False
            )


            # ---------------------
            # Run Crew
            # ---------------------
            result = crew.kickoff(
                inputs=inputs
            )


        # -------------------------
        # Display Final Result
        # -------------------------
        st.markdown("## 💡 CodeMentor AI Response")

        # Handles both string and CrewOutput object formats seamlessly
        output_text = result.raw if hasattr(result, "raw") else str(result)
        st.markdown(output_text)


    except Exception as e:

        st.error("Something went wrong.")

        st.code(str(e))

        st.info(
            "If this is a dependency or provider error, "
            "check the Streamlit deployment logs."
        )

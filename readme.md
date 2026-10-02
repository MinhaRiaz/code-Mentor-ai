 CodeMentor AI
CodeMentor AI is a multi-agent educational platform that generates highly personalized programming roadmaps and beginner-friendly syntax guides in seconds.

Built for the PakAngel’s Generative AI Hackathon, this application leverages agentic orchestration to replace generic tutorials with customized, phased learning paths tailored exactly to a user's experience level and goals.

🚀 Live Demo
Try the application live: "https://code-mentor-ai-app01.streamlit.app/"

🧠 The Agentic Architecture
Rather than relying on a single zero-shot LLM prompt, CodeMentor AI utilizes CrewAI to orchestrate a sequential pipeline of specialized AI personas. Each agent executes a distinct task, passing its output to the next for refinement.

🟢 Coding Expert: Analyzes the user's request and writes foundational, jargon-free syntax explanations and code snippets.

🔵 Learning Planner: Ingests the technical concepts and structures a phased, chronological roadmap to take the user from beginner to practical project execution.

🟣 Technical Reviewer: Acts as the senior editor, merging the syntax guide and roadmap into a unified, highly polished masterclass format, eliminating redundancies and ensuring pedagogical clarity.

✨ Key Features
Multi-Agent Orchestration: Transparent, sequential processing using CrewAI.

Live Status Tracking: A dynamic frontend UI that visualizes the agents' collaborative thought process in real-time.

Modern UI/UX: A highly polished, responsive Streamlit interface featuring custom CSS, gradient themes, and native Material Icons.

Resilient Infrastructure: Built-in error handling and graceful fallbacks for API rate limits and high-traffic spikes (503 Service Unavailable).

🛠️ Tech Stack
Frontend: Streamlit (Python) + Custom CSS + Google Material Icons

Agent Framework: CrewAI (Process.sequential)

LLM Provider: Google Gemini API (gemini-3.5-flash-lite) via crewai[google-genai] integration

Deployment: Streamlit Community Cloud

💻 Local Installation
To run this project locally on your machine, follow these steps:

1. Clone the repository
Bash
git clone https://github.com/yourusername/code-mentor-ai.git
cd code-mentor-ai
2. Install dependencies
Ensure you are using Python 3.11 for maximum compatibility.

Bash
pip install -r requirements.txt
3. Configure API Keys
Create a .streamlit folder in the root directory and add a secrets.toml file to securely store your Google Gemini API key.

Bash
mkdir .streamlit
touch .streamlit/secrets.toml
Add the following to your secrets.toml file:

Ini, TOML
GEMINI_API_KEY = "your_actual_api_key_here"
4. Run the application
Bash
streamlit run app.py
📁 Project Structure
Plaintext
CodeMentor_AI/
│
├── app.py                 # Streamlit frontend & UI logic
├── agents.py              # CrewAI agent definitions & personas
├── tasks.py               # Task allocations & expected outputs
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
│
└── .streamlit/
    └── secrets.toml       # Environment variables (not tracked in Git)
🤝 Contributing
Contributions, issues, and feature requests are welcome!
If you would like to expand this project (e.g., integrating n8n webhooks for course delivery automation, or adding code execution environments), feel free to submit a pull request.

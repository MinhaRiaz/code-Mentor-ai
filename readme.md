# 👨‍💻 CodeMentor AI

CodeMentor AI is a beginner-friendly Multi-Agent AI coding mentor built with Streamlit, CrewAI and Groq.

The application uses multiple specialized AI agents to help learners understand programming concepts and create a learning roadmap.

## 🤖 AI Agents

### Agent 1 — Programming Fundamentals Expert

Explains programming concepts and fundamentals using simple language and examples.

### Agent 2 — Programming Learning Planner

Creates a structured learning roadmap from fundamentals to practical projects.

### Agent 3 — Senior Beginner-Friendly Code Mentor

Reviews the previous agents' work and creates the final response.

## Technologies

- Python
- Streamlit
- CrewAI
- Groq
- GPT-OSS 120B

## Project Structure

```text
CodeMentor_AI/
│
├── app.py
├── agents.py
├── tasks.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml.example
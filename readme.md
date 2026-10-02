#  CodeMentor AI

### Multi-Agent AI Programming Mentor & Personalized Learning Roadmap Generator

**CodeMentor AI** is a multi-agent educational platform that helps beginners learn programming through **personalized syntax guides, structured learning roadmaps, and practical project guidance**.

Built for the **Pak Angels Generative AI Hackathon**, CodeMentor AI uses **CrewAI** to orchestrate multiple specialized AI agents. Instead of providing a generic programming tutorial, the system analyzes the learner's request and generates a customized learning experience based on their **skill level, programming language, and learning goals**.

---

## 🚀 Live Demo

Try CodeMentor AI:

**https://code-mentor-ai-app01.streamlit.app/**

---

## 🎯 Problem Statement

Many beginners struggle with programming because existing tutorials often provide:

* Generic learning paths
* Too much technical jargon
* Content that is not adapted to the learner's level
* No clear progression from syntax to practical projects
* Difficulty knowing what to learn next

A learner may understand individual programming concepts but still not know **how those concepts fit together into a practical learning journey**.

### 💡 Our Solution

CodeMentor AI combines multiple specialized AI agents to transform a user's programming request into:

1. Beginner-friendly syntax explanations
2. Practical code examples
3. A structured learning roadmap
4. Recommended progression from fundamentals to projects
5. A final reviewed and unified learning guide

---

# 🧠 Agentic Architecture

CodeMentor AI uses **CrewAI with a sequential multi-agent workflow**.

Each agent has a specific responsibility and passes its output to the next agent.

```text
                    USER INPUT
                        │
                        ▼
              ┌───────────────────┐
              │   Coding Expert   │
              │                   │
              │ Syntax + Concepts │
              │ + Code Examples   │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Learning Planner  │
              │                   │
              │ Phased Roadmap    │
              │ + Progression     │
              └─────────┬─────────┘
                        │
                        ▼
              ┌───────────────────┐
              │ Technical Reviewer│
              │                   │
              │ Review + Refine   │
              │ + Final Masterclass│
              └─────────┬─────────┘
                        │
                        ▼
                 FINAL RESPONSE
```

---

## 🤖 AI Agents

### 🟢 1. Coding Expert

The Coding Expert focuses on understanding the learner's programming request and creating the technical foundation.

**Responsibilities:**

* Analyze the user's programming goal
* Identify required concepts
* Explain syntax in beginner-friendly language
* Avoid unnecessary technical jargon
* Provide simple code examples
* Connect syntax with practical usage

**Output:**

A foundational programming syntax and concept guide.

---

### 🔵 2. Learning Planner

The Learning Planner takes the technical concepts identified by the Coding Expert and organizes them into a structured learning path.

**Responsibilities:**

* Organize concepts in chronological order
* Define learning phases
* Move from fundamentals to practical implementation
* Recommend practice activities
* Suggest suitable project progression
* Prevent unnecessary jumps in difficulty

**Output:**

A personalized, phased programming roadmap.

---

### 🟣 3. Technical Reviewer

The Technical Reviewer acts as the senior editor of the pipeline.

It receives the outputs from the previous agents and combines them into one polished learning experience.

**Responsibilities:**

* Review generated content
* Remove unnecessary repetition
* Improve clarity and consistency
* Ensure concepts appear in a logical order
* Merge syntax explanations with the roadmap
* Improve beginner accessibility
* Produce the final masterclass-style response

**Output:**

A unified and refined programming learning guide.

---

# ✨ Key Features

## 🤖 Multi-Agent Orchestration

CodeMentor AI uses multiple specialized agents instead of relying on a single LLM prompt.

The agents collaborate sequentially to produce a more structured educational response.

---

## 🧭 Personalized Learning Roadmaps

The generated roadmap is adapted to the learner's:

* Programming language
* Current experience level
* Learning objectives
* Required concepts
* Desired practical outcome

---

## 📚 Beginner-Friendly Syntax Guides

Programming concepts are explained using:

* Simple terminology
* Clear explanations
* Practical examples
* Beginner-friendly code snippets
* Logical progression

The goal is to make programming concepts easier to understand without overwhelming new learners.

---

## 📈 Phased Learning

Instead of presenting a large list of programming topics, CodeMentor AI organizes learning into progressive stages.

For example:

```text
Phase 1
Programming Fundamentals
        ↓
Phase 2
Variables & Control Flow
        ↓
Phase 3
Functions & Data Structures
        ↓
Phase 4
Object-Oriented Programming
        ↓
Phase 5
Practical Projects
```

This allows learners to understand **what to learn, when to learn it, and why it matters**.

---

## 🔄 Live Agent Status Tracking

The Streamlit interface provides dynamic status feedback while the multi-agent workflow is running.

Users can see which stage of the AI workflow is currently being processed.

Example:

```text
✓ Coding Expert
  Generating syntax guide...

✓ Learning Planner
  Building personalized roadmap...

✓ Technical Reviewer
  Refining final learning guide...

✓ Complete
  Your CodeMentor roadmap is ready!
```

---

## 🎨 Modern User Interface

The application uses Streamlit with custom CSS to provide a modern educational experience.

The interface includes:

* Responsive layout
* Gradient-based visual design
* Custom styling
* Google Material Icons
* Agent status indicators
* Clear content sections
* Interactive user inputs

---

## 🛡️ Resilient Infrastructure

The application includes error handling for common API and deployment issues.

The system is designed to gracefully handle situations such as:

* API failures
* Rate limits
* Temporary service interruptions
* High traffic
* Model availability issues

---

# 🛠️ Tech Stack

| Technology                    | Purpose                      |
| ----------------------------- | ---------------------------- |
| **Python**                    | Core application language    |
| **Streamlit**                 | Frontend and web application |
| **CrewAI**                    | Multi-agent orchestration    |
| **Google Gemini API**         | Large Language Model         |
| **crewai[google-genai]**      | Gemini integration           |
| **Custom CSS**                | UI styling                   |
| **Google Material Icons**     | Interface icons              |
| **Streamlit Community Cloud** | Deployment                   |

### LLM

```text
Google Gemini
gemini-3.5-flash-lite
```

### Agent Process

```text
CrewAI
Process.sequential
```

---

# 📁 Project Structure

```text
CodeMentor_AI/
│
├── app.py
│   └── Streamlit frontend and application logic
│
├── agents.py
│   └── CrewAI agent definitions and personas
│
├── tasks.py
│   └── Agent tasks and expected outputs
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│   └── Project documentation
│
└── .streamlit/
    └── secrets.toml
        └── API keys and environment secrets
```

---

# 💻 Local Installation

Follow these steps to run CodeMentor AI locally.

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/code-mentor-ai.git
cd code-mentor-ai
```

> Replace `yourusername` with your actual GitHub username and repository name.

---

## 2. Create a Virtual Environment

Python **3.11** is recommended for compatibility.

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 4. Configure the Gemini API Key

Create a `.streamlit` directory in the project root:

```text
CodeMentor_AI/
└── .streamlit/
```

Inside it, create:

```text
secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "your_actual_api_key_here"
```

### ⚠️ Important

Never commit your API key to GitHub.

Add the following to your `.gitignore`:

```text
.streamlit/secrets.toml
venv/
__pycache__/
*.pyc
```

---

# ▶️ 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🔐 Environment Configuration

CodeMentor AI expects the following secret:

| Variable         | Description                          |
| ---------------- | ------------------------------------ |
| `GEMINI_API_KEY` | Google Gemini API authentication key |

For Streamlit Community Cloud, add the key through:

```text
App Settings
      ↓
Secrets
      ↓
GEMINI_API_KEY
```

Do not place private API keys directly inside the Python source code.

---

# ☁️ Deployment

CodeMentor AI is deployed using **Streamlit Community Cloud**.

General deployment workflow:

```text
Local Project
     │
     ▼
GitHub Repository
     │
     ▼
Streamlit Community Cloud
     │
     ▼
Configure GEMINI_API_KEY
     │
     ▼
Deploy
     │
     ▼
Live Application
```

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main application file.
5. Add `GEMINI_API_KEY` to Streamlit Secrets.
6. Deploy the application.

---

# 📋 Example Use Cases

CodeMentor AI can help learners with requests such as:

### Python

```text
I am a complete beginner. Teach me Python basics
and create a roadmap that eventually helps me build
a simple automation project.
```

### Java

```text
I know basic programming but am new to Java.
Explain Java syntax and give me a roadmap toward
Object-Oriented Programming.
```

### Flutter

```text
I am new to Flutter. Explain the basic syntax and
create a roadmap that helps me eventually build
mobile applications.
```

### JavaScript

```text
I know basic programming concepts but have never
used JavaScript. Give me a beginner-friendly guide
and a roadmap toward building web applications.
```

---

# 🔄 How the Workflow Works

When a user submits a request, CodeMentor AI follows this pipeline:

### Step 1 — User Input

The learner provides information such as:

```text
Programming Language
Experience Level
Learning Goal
Specific Topic
```

↓

### Step 2 — Coding Expert

The agent analyzes the request and generates:

```text
Concepts
Syntax
Examples
Fundamentals
```

↓

### Step 3 — Learning Planner

The planner transforms those concepts into:

```text
Phase 1
Phase 2
Phase 3
Phase 4
Projects
Practice
```

↓

### Step 4 — Technical Reviewer

The reviewer combines the generated outputs and improves:

```text
Accuracy
Clarity
Organization
Consistency
Beginner Friendliness
```

↓

### Step 5 — Final Learning Guide

The user receives a complete personalized programming guide.

---

# 🏗️ Why Multi-Agent AI?

A single AI prompt can generate programming explanations, but CodeMentor AI separates the educational workflow into specialized responsibilities.

Each agent focuses on a different part of the problem:

| Agent                 | Primary Responsibility                |
| --------------------- | ------------------------------------- |
| 🟢 Coding Expert      | Technical concepts and syntax         |
| 🔵 Learning Planner   | Learning sequence and roadmap         |
| 🟣 Technical Reviewer | Quality control and final integration |

This separation allows the application to treat **content generation, curriculum planning, and review as distinct stages**.

---

# 🎓 Hackathon Project

CodeMentor AI was developed for the:

### **Pak Angels Generative AI Hackathon**

The project demonstrates practical use of:

* Generative AI
* Agentic AI
* Multi-agent orchestration
* Educational AI
* Personalized learning
* LLM-powered content generation
* Cloud deployment

The core objective is to demonstrate how agentic workflows can be applied to create a more personalized programming-learning experience.

---

# 🚀 Future Improvements

Potential future improvements include:

### 📚 Course Delivery Automation

Integrate **n8n workflows** to automatically deliver:

* Daily lessons
* Practice exercises
* Learning reminders
* Progress updates

### 💻 Code Execution

Add a secure code execution environment so learners can:

* Run generated examples
* Test their solutions
* Receive feedback
* Practice directly inside the platform

### 📊 Learning Progress Tracking

Add learner profiles with:

* Completed topics
* Progress percentage
* Learning history
* Project milestones

### 🧪 Interactive Quizzes

Generate quizzes automatically based on the concepts covered in each learning phase.

### 🤝 AI Coding Mentor

Add a conversational mentor that allows learners to ask follow-up questions while progressing through their roadmap.

---

# 🤝 Contributing

Contributions are welcome!

If you have an idea for improving CodeMentor AI, you can:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

Example:

```bash
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push origin feature/new-feature
```

Suggestions and feature ideas are also welcome through GitHub Issues.

---

# 📄 License

This project is intended for educational and hackathon purposes.

If you plan to publish the repository publicly, consider adding an appropriate open-source license such as **MIT License**.

---

# 👩‍💻 Project

**CodeMentor AI**

> Learn smarter. Code better. Build your path.

**Live Demo:**
https://code-mentor-ai-app01.streamlit.app/

**Built with:** Python · Streamlit · CrewAI · Google Gemini

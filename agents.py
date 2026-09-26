import os
from crewai import Agent, LLM

def create_agents(api_key: str):
    # Pass the key to OS environment for LiteLLM routing
    os.environ["GEMINI_API_KEY"] = api_key

    # Define Gemini 1.5 Flash model
    gemini_llm = LLM(
        model="gemini/gemini-1.5-flash",
        api_key=api_key
    )

    coding_agent = Agent(
        role="Coding Expert",
        goal="Explain {language} fundamentals clearly for a {level} learner.",
        backstory="You are an expert developer who excels at explaining programming syntax and foundational concepts simply.",
        llm=gemini_llm
    )

    learning_agent = Agent(
        role="Learning Planner",
        goal="Design a structured learning roadmap for {language} tailored to a {level} level.",
        backstory="You are an educational strategist who breaks programming down into actionable, sequential milestones.",
        llm=gemini_llm
    )

    reviewer_agent = Agent(
        role="Reviewer Agent",
        goal="Synthesize explanations and learning roadmaps into a cohesive, beginner-friendly guide.",
        backstory="You are a technical editor ensuring that concepts and roadmaps flow together without repetition.",
        llm=gemini_llm
    )

    return coding_agent, learning_agent, reviewer_agent

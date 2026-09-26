from crewai import Agent, LLM


def create_agents(api_key):

    # -----------------------------
    # Shared LLM
    # -----------------------------
    llm = LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0.3
    )


    # -----------------------------
    # Agent 1
    # -----------------------------
    coding_agent = Agent(

        role="Programming Fundamentals Expert",

        goal=(
            "Explain programming concepts and fundamentals "
            "clearly to the learner."
        ),

        backstory=(
            "You are a patient programming teacher who specializes "
            "in beginner-friendly explanations and small practical examples."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False
    )


    # -----------------------------
    # Agent 2
    # -----------------------------
    learning_agent = Agent(

        role="Programming Learning Planner",

        goal=(
            "Create a logical and practical learning roadmap "
            "for the learner."
        ),

        backstory=(
            "You are an experienced programming mentor who organizes "
            "learning from fundamentals to practical projects."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False
    )


    # -----------------------------
    # Agent 3
    # -----------------------------
    reviewer_agent = Agent(

        role="Senior Beginner-Friendly Code Mentor",

        goal=(
            "Review the work of the other agents and produce "
            "one clear and accurate final response."
        ),

        backstory=(
            "You are a senior coding mentor and technical editor. "
            "You remove confusion, correct unclear explanations, "
            "and make technical content beginner-friendly."
        ),

        llm=llm,

        verbose=False,

        allow_delegation=False
    )


    return (
        coding_agent,
        learning_agent,
        reviewer_agent
    )
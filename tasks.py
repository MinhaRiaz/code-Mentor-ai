from crewai import Task

def create_tasks(coding_agent, learning_agent, reviewer_agent):

    coding_task = Task(
        description=(
            "Answer the user's question: '{question}' for language '{language}'. "
            "Provide key fundamental concepts and basic code examples suitable for a {level}."
        ),
        expected_output="A structured explanation of core programming concepts and code syntax examples.",
        agent=coding_agent
    )

    roadmap_task = Task(
        description=(
            "Create a step-by-step roadmap for learning {language} targeting a {level} learner, "
            "addressing their request: '{question}'."
        ),
        expected_output="A clear, phased learning path from current level to practical projects.",
        agent=learning_agent
    )

    review_task = Task(
        description=(
            "Combine the core explanations from the Coding Expert and the roadmap from the Learning Planner "
            "into a clean, unified response for the user."
        ),
        expected_output="A cohesive final response formatted cleanly with Markdown headings.",
        agent=reviewer_agent
    )

    return coding_task, roadmap_task, review_task

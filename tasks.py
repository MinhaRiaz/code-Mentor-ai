from crewai import Task


def create_tasks(
    coding_agent,
    learning_agent,
    reviewer_agent
):

    # -----------------------------
    # Task 1
    # -----------------------------
    coding_task = Task(

        description="""
The learner wants help with {language}.

Learner level:
{level}

Question:
{question}

Explain the relevant programming fundamentals
in simple language.

Include small practical examples where useful.

Focus on helping the learner understand the
concept instead of overwhelming them with
advanced terminology.
""",

        expected_output=(
            "A clear beginner-friendly explanation "
            "with simple examples."
        ),

        agent=coding_agent
    )


    # -----------------------------
    # Task 2
    # -----------------------------
    roadmap_task = Task(

        description="""
Create a learning roadmap for {language}.

Learner level:
{level}

Question:
{question}

Organize the roadmap from fundamentals
toward practical projects.

For every major stage, briefly explain
what the learner should learn.
""",

        expected_output=(
            "A structured programming roadmap "
            "with stages and explanations."
        ),

        agent=learning_agent
    )


    # -----------------------------
    # Task 3
    # -----------------------------
    review_task = Task(

        description="""
Create the final response for the learner.

Use the programming explanation and learning
roadmap created by the previous agents.

Requirements:

1. Directly answer the learner.
2. Use simple language.
3. Include examples where useful.
4. Include a logical roadmap.
5. Explain each roadmap stage briefly.
6. Suggest what the learner should do next.
7. Avoid unnecessary advanced topics.
8. Make the response practical.
9. Never claim that code was executed or tested.

Programming Language:
{language}

Learner Level:
{level}

Question:
{question}
""",

        expected_output=(
            "One polished beginner-friendly response "
            "combining the programming explanation "
            "and learning roadmap."
        ),

        agent=reviewer_agent,

        context=[
            coding_task,
            roadmap_task
        ]
    )


    return (
        coding_task,
        roadmap_task,
        review_task
    )
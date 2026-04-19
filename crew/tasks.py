from crewai import Task
from agents.researcher import research_agent
from agents.summarizer import summary_agent

def create_tasks(user_query):

    research_task = Task(
        description=f"""
        First check memory using 'search_memory'.

        If not found, use 'search_the_internet'.

        Query: {user_query}

        STRICT RULE:
        - Use ONLY available tools
        - Do NOT use any other tool
        """,
        agent=research_agent,
        expected_output="Accurate legal data"
    )

    summary_task = Task(
        description="""
        Summarize the information clearly.

        Then store important knowledge using 'store_memory'.
        """,
        agent=summary_agent,
        expected_output="Final answer"
    )

    return [research_task, summary_task]
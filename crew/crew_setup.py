from crewai import Crew
from crew.tasks import create_tasks
from agents.researcher import research_agent
from agents.summarizer import summary_agent

def run_crew(query):

    tasks = create_tasks(query)

    crew = Crew(
        agents=[research_agent, summary_agent],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    if hasattr(result, "raw"):
        return result.raw
    else:
        return str(result)
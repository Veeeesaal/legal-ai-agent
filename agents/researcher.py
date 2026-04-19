from crewai import Agent
from tools.crewai_llm import groq_llm
from tools.crewai_tools import search_internet
from tools.memory_crewai_tool import search_memory

research_agent = Agent(
    role="Legal Researcher",
    goal="Find accurate legal information using ONLY the provided tools",
    backstory="""
    You are a legal researcher.

    RULES:
    - First use 'search_memory'
    - If not found, use 'search_the_internet'
    - Do NOT use any other tools
    """,
    verbose=True,
    allow_delegation=False,
    llm=groq_llm,
    tools=[search_internet, search_memory]
)
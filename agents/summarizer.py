from crewai import Agent
from tools.crewai_llm import groq_llm
from tools.memory_crewai_tool import store_memory

summary_agent = Agent(
    role="Legal Summarizer",
    goal="Summarize legal information clearly",
    backstory="""
    You are an expert legal summarizer.

    STRICT RULES:
    - DO NOT use any tool except 'store_memory'
    - DO NOT try to call 'summarize' or any other tool
    - Just directly generate the summary text
    - After summarizing, store it using 'store_memory'
    """,
    verbose=True,
    allow_delegation=False,
    llm=groq_llm,
    tools=[store_memory]
)
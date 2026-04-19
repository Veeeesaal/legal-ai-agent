from crewai.tools import tool
from tools.memory_tool import Memory

memory = Memory()

@tool("search_memory")
def search_memory(query: str) -> str:
    """Search past stored legal knowledge"""
    return memory.search(query)


@tool("store_memory")
def store_memory(data: str) -> str:
    """Store important legal information for future use"""
    memory.add(data)
    return "Stored successfully"
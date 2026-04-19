from crewai.tools import tool
from tools.search_tool import search_tool

@tool("search_the_internet")   
def search_internet(query: str) -> str:
    """Search the internet for legal information and return results"""
    return search_tool(query)
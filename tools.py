from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

search_engine = DuckDuckGoSearchRun()
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_engine = WikipediaQueryRun(api_wrapper=api_wrapper)

def search_tool(query: str) -> str:
    """Search the web for information using DuckDuckGo"""
    return search_engine.run(query)

def wiki_tool(query: str) -> str:
    """Search Wikipedia for information"""
    return wiki_engine.run(query)

def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """Saves structured research data to a text file"""
    return save_to_txt(data, filename)

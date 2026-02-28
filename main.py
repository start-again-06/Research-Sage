from pydantic_ai import Agent
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from tools import search_tool, wiki_tool, save_tool
 
load_dotenv()
 
class ResearchSummary(BaseModel):
    """A structured summary of web research results."""
    
    topic: str = Field(
        ..., 
        description="The primary topic of the research query."
    )
    report: str = Field(
        ..., 
        description="A detailed report on the topic."
    )
    source_confidence_score: float = Field(
        ..., 
        description="A score from 0.0 to 1.0 indicating confidence in the factual accuracy of the results, based on source quality."
    )    
 
def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY environment variable is required. "            
            "Please set it in your .env file or environment variables."
        )
    
    agent = Agent(
        model="openrouter:openai/gpt-oss-120b:free",
        output_type=ResearchSummary,
        system_prompt=(
            """You are a research assistant and your job is to research the topic provided 
            and return a detailed report on the topic. Use the available search tools to find 
            current information and return a comprehensive report with a confidence score based 
            on the quality and recency of your sources."""
        ),
        tools=[search_tool, wiki_tool]

    )
    

    result = agent.run_sync("What are the latest developments in quantum computing?")
 
    
    data = result.output
    print(f"Topic: {data.topic}")
    print(f"Report: {data.report}")
    print(f"Confidence: {data.source_confidence_score}")
 
if __name__ == "__main__":
    main()

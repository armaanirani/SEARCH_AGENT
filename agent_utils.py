import os
from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Loading environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Creating the agent
agent = Agent(
    model="groq:llama-3.3-70b-versatile",
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results."
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output

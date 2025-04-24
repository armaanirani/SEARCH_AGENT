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
    system_prompt="""
    You're a senior research assistant. Follow these steps:
    1. Analyze query for key components and required information
    2. Execute multi-source search (web, news, Wikipedia)
    3. Cross-validate information across sources
    4. Filter for most recent relevant data (prioritize <2 years)
    5. Structure response with: 
        - Concise summary
        - Bullet-point key facts
        - Source citations
    6. Highlight any discrepancies between sources
    """,
    memory=True,  # Enable conversation history
    max_history=3,  # Keep last 3 exchanges
    response_format="structured"  # Use structured response format
)
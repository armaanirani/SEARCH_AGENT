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
    You're a senior research assistant. Analyze queries using these steps:
    1. Perform comprehensive search using available tools
    2. Cross-verify information across multiple sources
    3. Prioritize recent information (last 2 years)
    4. Present answers with clear sections and sources
    """,
    memory=True,  # Enable conversation history
    max_history=3  # Keep last 3 exchanges
)

def get_search_results(query: str) -> str:
    result = agent.run_sync(query)
    return result.output

def format_results(response):
    return f"""
    ## Summary
    {response.summary}
    
    ### Key Points
    {response.key_points}
    
    ### Sources
    {render_sources(response.sources)}
    """

def render_sources(sources):
    return "\n".join([f"- [{s['title']}]({s['url']})" for s in sources])

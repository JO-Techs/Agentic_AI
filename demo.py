from langchain.agents import initialize_agent, AgentType
from langchain.agents.tools import Tool
from langchain.llms import OpenAI
from langchain.tools import tool
import requests
import os

# Set OpenAI API key (Replace with your key or set via environment variable)
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

# Define a simple calculator tool
def calculator(expression: str) -> str:
    """Evaluates a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

# Define a basic web search tool
def web_search(query: str) -> str:
    """Performs a web search and returns the top result."""
    response = requests.get(f"https://www.googleapis.com/customsearch/v1?q={query}&key=your-google-api-key&cx=your-search-engine-id")
    if response.status_code == 200:
        results = response.json().get("items", [])
        return results[0]["snippet"] if results else "No results found."
    return "Search failed."

# Register tools
calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Use this tool to evaluate mathematical expressions."")
)

web_search_tool = Tool(
    name="Web Search",
    func=web_search,
    description="Use this tool to search the web for recent information."
)

# Initialize the agent
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[calculator_tool, web_search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run the agent with a query
response = agent.run("What is the square root of 256 plus the population of India?")
print(response)

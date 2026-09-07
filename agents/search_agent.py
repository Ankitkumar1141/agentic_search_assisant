from langchain.agents import create_agent

from agents.llm import get_mistral_llm
from prompts.search_prompt import SEARCH_SYSTEM_PROMPT, SEARCH_USER_TEMPLATE
from tools.web_search import web_search


def build_search_agent():
    """Build the search agent that queries the web via Tavily."""
    return create_agent(
        model=get_mistral_llm(),
        tools=[web_search],
        system_prompt=SEARCH_SYSTEM_PROMPT,
    )


def run_search_agent(topic: str) -> str:
    """Run the search agent for a given topic and return its response."""
    agent = build_search_agent()
    result = agent.invoke(
        {"messages": [("user", SEARCH_USER_TEMPLATE.format(topic=topic))]}
    )
    return result["messages"][-1].content

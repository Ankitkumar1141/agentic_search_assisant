from langchain.agents import create_agent

from agents.llm import get_mistral_llm
from prompts.reader_prompt import READER_SYSTEM_PROMPT, READER_USER_TEMPLATE
from tools.web_scraper import scrape_url


def build_reader_agent():
    """Build the reader agent that scrapes URLs for deeper content."""
    return create_agent(
        model=get_mistral_llm(),
        tools=[scrape_url],
        system_prompt=READER_SYSTEM_PROMPT,
    )


def run_reader_agent(topic: str, search_results: str, preview_chars: int = 800) -> str:
    """Run the reader agent using truncated search results as context."""
    agent = build_reader_agent()
    preview = search_results[:preview_chars]
    result = agent.invoke(
        {
            "messages": [
                (
                    "user",
                    READER_USER_TEMPLATE.format(topic=topic, search_results=preview),
                )
            ]
        }
    )
    return result["messages"][-1].content

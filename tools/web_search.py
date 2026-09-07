from langchain.tools import tool
from tavily import TavilyClient

from config.settings import TAVILY_API_KEY, TAVILY_MAX_RESULTS
from utils.logger import get_logger

logger = get_logger(__name__)

_tavily = TavilyClient(api_key=TAVILY_API_KEY) if TAVILY_API_KEY else None


@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Returns titles, URLs, and snippets."""
    if not _tavily:
        return "Error: TAVILY_API_KEY is not configured."

    logger.info("Searching the web for: %s", query)
    results = _tavily.search(query=query, max_results=TAVILY_MAX_RESULTS)

    out = []
    for result in results.get("results", []):
        snippet = result.get("content", "")[:300]
        out.append(
            f"Title: {result.get('title', 'N/A')}\n"
            f"URL: {result.get('url', 'N/A')}\n"
            f"Snippet: {snippet}\n"
        )

    return "\n----\n".join(out) if out else "No search results found."

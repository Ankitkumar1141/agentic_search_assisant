import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

from config.settings import SCRAPE_MAX_CHARS, SCRAPE_TIMEOUT_SECONDS
from utils.logger import get_logger

logger = get_logger(__name__)


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        logger.info("Scraping URL: %s", url)
        response = requests.get(
            url,
            timeout=SCRAPE_TIMEOUT_SECONDS,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        return soup.get_text(separator=" ", strip=True)[:SCRAPE_MAX_CHARS]
    except Exception as exc:
        logger.warning("Failed to scrape %s: %s", url, exc)
        return f"Could not scrape URL: {exc}"

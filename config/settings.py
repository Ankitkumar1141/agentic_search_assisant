import os

from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY: str | None = os.getenv("MISTRAL_API_KEY")
TAVILY_API_KEY: str | None = os.getenv("TAVILY_API_KEY")
MISTRAL_MODEL: str = os.getenv("MISTRAL_MODEL", "mistral-small-latest")
MISTRAL_TEMPERATURE: float = float(os.getenv("MISTRAL_TEMPERATURE", "0"))

SCRAPE_TIMEOUT_SECONDS: int = int(os.getenv("SCRAPE_TIMEOUT_SECONDS", "8"))
SCRAPE_MAX_CHARS: int = int(os.getenv("SCRAPE_MAX_CHARS", "3000"))
TAVILY_MAX_RESULTS: int = int(os.getenv("TAVILY_MAX_RESULTS", "5"))

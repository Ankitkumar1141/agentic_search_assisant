from langchain_mistralai import ChatMistralAI

from config.settings import MISTRAL_API_KEY, MISTRAL_MODEL, MISTRAL_TEMPERATURE


def get_mistral_llm() -> ChatMistralAI:
    """Return a configured Mistral chat model instance."""
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY is not configured. Set it in your .env file.")

    return ChatMistralAI(
        model=MISTRAL_MODEL,
        temperature=MISTRAL_TEMPERATURE,
        api_key=MISTRAL_API_KEY,
    )

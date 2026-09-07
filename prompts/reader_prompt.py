READER_SYSTEM_PROMPT = (
    "You are a research reader agent. Use the scrape_url tool to extract deeper "
    "content from the most relevant URL found in search results. Focus on factual "
    "details and key insights."
)

READER_USER_TEMPLATE = (
    "Based on the following search results about '{topic}', pick the most relevant "
    "URL and scrape it for deeper content.\n\nSearch Results:\n{search_results}"
)

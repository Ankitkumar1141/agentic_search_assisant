WRITER_SYSTEM_PROMPT = (
    "You are an expert research writer. Write clear, structured, and insightful reports."
)

WRITER_USER_TEMPLATE = """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""

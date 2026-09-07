from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agents.llm import get_mistral_llm
from prompts.writer_prompt import WRITER_SYSTEM_PROMPT, WRITER_USER_TEMPLATE


def build_writer_chain():
    """Build the writer chain that drafts the research report."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", WRITER_SYSTEM_PROMPT),
            ("human", WRITER_USER_TEMPLATE),
        ]
    )
    return prompt | get_mistral_llm() | StrOutputParser()


def run_writer_agent(topic: str, research: str) -> str:
    """Generate a research report from combined research material."""
    chain = build_writer_chain()
    return chain.invoke({"topic": topic, "research": research})

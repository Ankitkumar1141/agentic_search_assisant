from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agents.llm import get_mistral_llm
from prompts.critic_prompt import CRITIC_SYSTEM_PROMPT, CRITIC_USER_TEMPLATE


def build_critic_chain():
    """Build the critic chain that reviews the research report."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", CRITIC_SYSTEM_PROMPT),
            ("human", CRITIC_USER_TEMPLATE),
        ]
    )
    return prompt | get_mistral_llm() | StrOutputParser()


def run_critic_agent(report: str) -> str:
    """Review a research report and return structured feedback."""
    chain = build_critic_chain()
    return chain.invoke({"report": report})

from agents.critic_agent import run_critic_agent
from agents.reader_agent import run_reader_agent
from agents.search_agent import run_search_agent
from agents.writer_agent import run_writer_agent
from schemas.research_state import ResearchState
from utils.logger import get_logger

logger = get_logger(__name__)


def run_research_pipeline(topic: str) -> ResearchState:
    """Execute the full multi-agent research workflow."""
    state = ResearchState(topic=topic)

    logger.info("Step 1 - Search agent is working...")
    state.search_results = run_search_agent(topic)
    logger.info("Search completed.")

    logger.info("Step 2 - Reader agent is scraping top resources...")
    state.scraped_content = run_reader_agent(topic, state.search_results)
    logger.info("Reader completed.")

    logger.info("Step 3 - Writer is drafting the report...")
    research_combined = (
        f"SEARCH RESULTS:\n{state.search_results}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state.scraped_content}"
    )
    state.report = run_writer_agent(topic, research_combined)
    logger.info("Writer completed.")

    logger.info("Step 4 - Critic is reviewing the report...")
    state.feedback = run_critic_agent(state.report)
    logger.info("Critic completed.")

    return state


if __name__ == "__main__":
    user_topic = input("\nEnter a research topic: ").strip()
    if user_topic:
        final_state = run_research_pipeline(user_topic)
        print("\n--- Final Report ---\n")
        print(final_state.report)
        print("\n--- Critic Feedback ---\n")
        print(final_state.feedback)

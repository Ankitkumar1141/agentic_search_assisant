from unittest.mock import MagicMock, patch

import pytest

from agents.search_agent import run_search_agent
from prompts.search_prompt import SEARCH_USER_TEMPLATE


@pytest.fixture
def mock_agent_response():
    mock_message = MagicMock()
    mock_message.content = "Title: Example\nURL: https://example.com\nSnippet: Test"
    return {"messages": [mock_message]}


@patch("agents.search_agent.build_search_agent")
def test_run_search_agent(mock_build_agent, mock_agent_response):
    mock_agent = MagicMock()
    mock_agent.invoke.return_value = mock_agent_response
    mock_build_agent.return_value = mock_agent

    topic = "quantum computing"
    result = run_search_agent(topic)

    assert "Example" in result
    mock_agent.invoke.assert_called_once_with(
        {"messages": [("user", SEARCH_USER_TEMPLATE.format(topic=topic))]}
    )


@patch("agents.search_agent.build_search_agent")
def test_search_agent_uses_mistral(mock_build_agent):
    with patch("agents.search_agent.get_mistral_llm") as mock_llm:
        mock_llm.return_value = MagicMock()
        mock_build_agent.return_value = MagicMock()

        from agents.search_agent import build_search_agent

        build_search_agent()
        mock_llm.assert_called_once()

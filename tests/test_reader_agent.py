from unittest.mock import MagicMock, patch

import pytest

from agents.reader_agent import run_reader_agent


@pytest.fixture
def mock_agent_response():
    mock_message = MagicMock()
    mock_message.content = "Scraped article content about the topic."
    return {"messages": [mock_message]}


@patch("agents.reader_agent.build_reader_agent")
def test_run_reader_agent(mock_build_agent, mock_agent_response):
    mock_agent = MagicMock()
    mock_agent.invoke.return_value = mock_agent_response
    mock_build_agent.return_value = mock_agent

    topic = "fusion energy"
    search_results = "Title: Fusion\nURL: https://example.com\nSnippet: Energy"
    result = run_reader_agent(topic, search_results)

    assert "Scraped article content" in result
    mock_agent.invoke.assert_called_once()


@patch("agents.reader_agent.get_mistral_llm")
def test_reader_agent_uses_mistral(mock_llm):
    mock_llm.return_value = MagicMock()

    with patch("agents.reader_agent.create_agent") as mock_create:
        mock_create.return_value = MagicMock()

        from agents.reader_agent import build_reader_agent

        build_reader_agent()
        mock_llm.assert_called_once()

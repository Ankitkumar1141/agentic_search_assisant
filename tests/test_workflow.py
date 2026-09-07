from unittest.mock import MagicMock, patch

import pytest

from schemas.research_state import ResearchState
from workflows.research_workflow import run_research_pipeline


@pytest.fixture
def mock_pipeline_outputs():
    return {
        "search": "Search results with https://example.com",
        "reader": "Detailed scraped content",
        "writer": "# Report\n\nIntroduction\n\nKey Findings\n\nConclusion",
        "feedback": "Score: 8/10\n\nStrengths:\n- Clear structure",
    }


@patch("workflows.research_workflow.run_critic_agent")
@patch("workflows.research_workflow.run_writer_agent")
@patch("workflows.research_workflow.run_reader_agent")
@patch("workflows.research_workflow.run_search_agent")
def test_run_research_pipeline(
    mock_search,
    mock_reader,
    mock_writer,
    mock_critic,
    mock_pipeline_outputs,
):
    mock_search.return_value = mock_pipeline_outputs["search"]
    mock_reader.return_value = mock_pipeline_outputs["reader"]
    mock_writer.return_value = mock_pipeline_outputs["writer"]
    mock_critic.return_value = mock_pipeline_outputs["feedback"]

    state = run_research_pipeline("AI agents")

    assert isinstance(state, ResearchState)
    assert state.topic == "AI agents"
    assert state.search_results == mock_pipeline_outputs["search"]
    assert state.scraped_content == mock_pipeline_outputs["reader"]
    assert state.report == mock_pipeline_outputs["writer"]
    assert state.feedback == mock_pipeline_outputs["feedback"]

    mock_search.assert_called_once_with("AI agents")
    mock_reader.assert_called_once_with("AI agents", mock_pipeline_outputs["search"])
    mock_writer.assert_called_once()
    mock_critic.assert_called_once_with(mock_pipeline_outputs["writer"])

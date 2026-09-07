# Agentic Research Assistant

A multi-agent research system that searches the web, scrapes content, writes a structured report, and critiques the output. The project recreates the demo **Multi-agent-research-system** with a modular architecture and uses **Mistral AI** as the sole LLM provider (no OpenAI/GPT, Gemini, or other models).

## Architecture

```text
User Topic
    │
    ▼
Search Agent  ──►  Tavily web search
    │
    ▼
Reader Agent  ──►  URL scraping (BeautifulSoup)
    │
    ▼
Writer Agent  ──►  Structured research report
    │
    ▼
Critic Agent  ──►  Score + feedback
```

## Project Structure

```text
agentic-research-assistant/
├── app.py                         # Streamlit application
├── agents/                        # Mistral-powered agents
├── workflows/research_workflow.py # Orchestrates all agents
├── tools/                         # Web search & scraping tools
├── prompts/                       # Agent prompt templates
├── schemas/research_state.py      # Shared workflow state
├── config/settings.py             # Environment configuration
├── utils/logger.py                # Logging helper
└── tests/                         # Unit tests
```

## Prerequisites

- Python 3.10+
- [Mistral AI API key](https://console.mistral.ai/)
- [Tavily API key](https://tavily.com/)

## Setup

1. Clone or copy the project and enter the directory:

```bash
cd agentic-research-assistant
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
copy .env.example .env
```

Edit `.env` and set:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
MISTRAL_MODEL=ministral-3b-2512
```

## Usage

### Streamlit UI

```bash
streamlit run app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`).

### CLI workflow

```bash
python -m workflows.research_workflow
```

### Run tests

```bash
pytest tests/ -v
```

## Docker

Build and run the Streamlit app in a container:

```bash
docker build -t agentic-research-assistant .
docker run -p 8501:8501 --env-file .env agentic-research-assistant
```

## Demo vs This Project

| Aspect | This Project |
|--------|------|--------------|
| LLM | Mistral AI |
| Structure | Modular packages |
| UI | Streamlit | 
| Search | Tavily | 
| Scraping | BeautifulSoup |

## License

MIT

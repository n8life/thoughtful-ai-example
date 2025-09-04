# Thoughtful AI Agent Example

A powerful AI-powered agent application that leverages OpenAI and LangChain to provide intelligent conversational interactions and automated task processing. This project demonstrates the integration of modern AI tools with efficient vector storage using FAISS for semantic search capabilities.

## Features

- **Intelligent Conversational AI**: Powered by OpenAI's language models for natural language understanding and generation
- **LangChain Integration**: Utilizes LangChain framework for building sophisticated AI applications with chain-of-thought reasoning
- **Vector Storage**: Implements FAISS indexing for efficient similarity search and retrieval
- **Configurable Environment**: Easy setup through environment variables
- **Scalable Architecture**: Designed with modular components for easy extension and customization

## Prerequisites

Before getting started, you'll need to obtain API keys from the following services:

- **OpenAI API Key**: Get yours at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **LangChain API Key** (for LangSmith tracing): Sign up at [https://docs.langchain.com/langsmith/create-account-api-key](https://docs.langchain.com/langsmith/create-account-api-key)
- **Astral UV**: Instructions for installing UV can be found [here](https://docs.astral.sh/uv/)
## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd thoughtful-ai-agent
```

### 2. Install Dependencies

This project uses `uv` for dependency management. Install the required packages:

```bash
uv sync
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=thoughtful-ai-agent
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

**Important Notes:**
- Replace `your_openai_api_key_here` with your actual OpenAI API key
- Replace `your_langchain_api_key_here` with your actual LangChain API key
- Set `LANGCHAIN_TRACING_V2=true` to enable LangSmith tracing for debugging and monitoring
- The `LANGCHAIN_PROJECT` name will appear in your LangSmith dashboard

## Running the Application

```bash
uv run main.py
```

## Project Structure

- `main.py` - Main application entry point
- `data.json` - Data storage for the agent
- `data_schema.json` - Schema definitions for data validation
- `faiss_index_react/` - FAISS vector index storage for semantic search
- `.env.sample` - Example environment configuration file

## Security

Never commit your `.env` file to version control. The `.gitignore` file is configured to exclude it automatically.
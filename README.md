# ITC RAG Chatbot

A retrieval-augmented generation (RAG) chatbot for **Into The Cryptoverse (ITC)** content, designed to answer subscriber questions using:

- ITC website content
- YouTube video transcripts (with recency awareness)
- Large Language Models (LLMs)

The system prioritizes **recent market commentary** while retaining historical context for past market cycles.

---

## Features (Planned)

- 🔎 Semantic + metadata-based retrieval
- 🧠 Recency-weighted document ranking
- 🎥 Automated ingestion of YouTube transcripts
- 🌐 Website crawling and document ingestion
- 💬 Conversational chat API (FastAPI)
- 📎 Source citation in responses
- 🚀 Deployment-ready architecture

---

## Tech Stack

- **Python** 3.12
- **Poetry** – dependency & environment management
- **LangChain** – RAG orchestration
- **ChromaDB** – vector storage
- **OpenAI** – embeddings & chat models
- **FastAPI** – API layer

---

## Project Structure

itc-rag-chatbot/
├── src/itc_rag_chatbot/
│ ├── ingestion/ # data ingestion pipelines
│ ├── rag/ # retrieval and prompting logic
│ ├── api/ # FastAPI application
│ └── utils/
├── data/ # local data and vector stores (gitignored)
├── notebooks/
├── tests/
├── pyproject.toml
├── poetry.lock
└── README.md

---

## Setup

```bash
poetry install --no-root
poetry shell

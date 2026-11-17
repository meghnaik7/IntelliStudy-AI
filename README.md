# 🎓 IntelliStudy-AI

An AI-powered study assistant built with LangChain that helps students learn smarter — through intelligent summarization, RAG-based Q&A over their own documents, auto-generated quizzes, and an agentic study workflow.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📚 **Study Assistant** | Generates structured study notes and explanations from any topic |
| 📄 **Document Q&A (RAG)** | Upload your PDFs/docs and ask questions grounded in your own material |
| 🧠 **Quiz Generation** | Auto-generates multiple-choice quizzes from topics or uploaded documents |
| ✅ **Quiz Evaluation** | Evaluates your answers and provides detailed feedback |
| 🤖 **Study Agent** | An autonomous agent that picks the right tool based on your query |
| 💬 **Chat History** | Maintains conversational context across multi-turn interactions |

---

## 🏗️ Project Structure

```
IntelliStudy-AI/
│
├── app/
│   ├── main.py                        # Single entry point
│   │
│   ├── config/
│   │   └── settings.py                # Environment & app configuration
│   │
│   ├── core/
│   │   ├── llm.py                     # LLM initialization (OpenAI / Groq etc.)
│   │   └── embeddings.py              # Embedding model setup
│   │
│   ├── prompts/
│   │   ├── study_prompt.py            # Prompt for study notes
│   │   ├── quiz_prompt.py             # Prompt for topic-based quiz
│   │   ├── document_quiz_prompt.py    # Prompt for document-based quiz
│   │   ├── rag_prompt.py              # Prompt for RAG Q&A
│   │   └── contextualize_prompt.py    # Prompt to contextualize follow-up questions
│   │
│   ├── chains/
│   │   ├── study_chain.py             # LangChain chain for study notes
│   │   ├── quiz_chain.py              # Chain for topic quiz generation
│   │   ├── document_quiz_chain.py     # Chain for document quiz generation
│   │   ├── rag_chain.py               # RAG chain for document Q&A
│   │   ├── contextualize_chain.py     # Chain for question contextualization
│   │   └── tool_chain.py              # Chain used by the agent tools
│   │
│   ├── schemas/
│   │   └── quiz.py                    # Pydantic schemas for quiz structure
│   │
│   ├── services/
│   │   ├── document_service.py        # PDF/document loading & chunking
│   │   ├── vector_service.py          # Vector store operations (Chroma/FAISS)
│   │   ├── rag_service.py             # RAG pipeline orchestration
│   │   ├── quiz_service.py            # Topic-based quiz orchestration
│   │   ├── quiz_evaluation.py         # Quiz answer evaluation logic
│   │   ├── document_quiz_service.py   # Document-based quiz orchestration
│   │   ├── chat_history_service.py    # Chat memory management
│   │   ├── tool_service.py            # Tool execution service
│   │   └── agent_service.py           # Agent orchestration service
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   └── study_tools.py             # LangChain tools exposed to the agent
│   │
│   └── agents/
│       ├── __init__.py
│       └── study_agent.py             # LangChain agent definition
│
├── vector_db/                         # Persisted vector store data
├── data/                              # User-uploaded documents
├── .env                               # API keys and environment variables
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/IntelliStudy-AI.git
cd IntelliStudy-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
# or
GROQ_API_KEY=your_groq_api_key
```

### 5. Run the app

```bash
python app/main.py
```

---

## 🧰 Tech Stack

- **[LangChain](https://www.langchain.com/)** — LLM orchestration, chains, agents, and tools
- **[OpenAI / Groq](https://groq.com/)** — LLM backend
- **[ChromaDB / FAISS](https://www.trychroma.com/)** — Vector store for RAG
- **[Pydantic](https://docs.pydantic.dev/)** — Data validation and schemas
- **Python 3.10+**

---

## 🗺️ Architecture Overview

```
User Query
    │
    ▼
Study Agent  ──────────────────────────────────────────┐
    │                                                   │
    ├── study_tools ──► study_chain ──► LLM            │
    │                                                   │
    ├── quiz_tools  ──► quiz_chain  ──► LLM + schema   │
    │                                                   │
    └── rag_tools   ──► vector_db  ──► rag_chain ──► LLM
                              ▲
                         document_service
                        (PDF ingestion &
                          chunking)
```

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

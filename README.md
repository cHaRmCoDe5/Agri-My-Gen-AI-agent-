# 🌾 AgriAssist-MY

An AI-powered Retrieval-Augmented Generation (RAG) application that helps users search and understand Malaysian agricultural schemes using natural language.

---

## 📌 Project Overview

AgriAssist-MY is a Generative AI application built with LangChain and OpenAI that retrieves information from Malaysian Department of Agriculture resources and provides accurate, context-aware answers.

Instead of searching through multiple webpages manually, users can simply ask questions in natural language and receive AI-generated responses backed by official information.

---

## ✨ Features

- 🤖 AI-powered question answering
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 Semantic search using embeddings
- ⚡ FAISS Vector Database
- 🌐 Streamlit web interface
- 📄 Automatic document ingestion
- 🧠 OpenAI GPT integration
- 🇲🇾 Focused on Malaysian agricultural schemes

---

## 🏗️ Project Architecture

```
User Question
      │
      ▼
Streamlit Frontend
      │
      ▼
RAG Pipeline
      │
      ├── Query Processing
      ├── Embedding Search
      ├── FAISS Retrieval
      ├── Context Builder
      └── OpenAI GPT
      │
      ▼
Generated Answer
```

---

## 📂 Project Structure

```
AgriAssist-MY
│
├── backend/
│   ├── embeddings/
│   ├── ingestion/
│   ├── rag/
│   ├── retrieval/
│   ├── reranker/
│   ├── vectorstore/
│   └── utils/
│
├── frontend/
│
├── data/
│   ├── documents/
│   ├── raw_html/
│   └── vectorstore/
│
├── requirements.txt
├── README.md
└── .env
```

---

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI GPT
- FAISS
- Streamlit
- BeautifulSoup
- Requests
- HTML Parsing
- Vector Embeddings

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/cHaRmCoDe5/Agri-My-Gen-AI-agent-.git
```

Move into the project

```bash
cd Agri-My-Gen-AI-agent-
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run frontend/app.py
```

---

## 💡 Example Questions

- What agricultural grants are available in Malaysia?
- What support does the Department of Agriculture provide?
- How do I apply for farming assistance?
- What are the eligibility criteria for government agricultural schemes?
- What incentives are available for young farmers?

---

## 🎯 Future Improvements

- Multi-language support (English, Malay, Tamil, Chinese)
- Voice input
- PDF document support
- Chat history
- User authentication
- Deployment to Streamlit Cloud

---

## 👨‍💻 Author

**Priya**

Built as a Generative AI RAG project using LangChain, OpenAI, FAISS, and Streamlit.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
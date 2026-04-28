# Financial RAG Chatbot – Intelligent Financial Knowledge Assistant

Financial RAG Chatbot is an AI-powered intelligent financial assistant built using Python, LangChain, LangGraph, FAISS, and OpenAI. This project uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers from financial documents such as annual reports, balance sheets, investment reports, bank statements, and policy documents.

Instead of relying only on a Large Language Model (LLM), the chatbot first retrieves relevant information from uploaded financial PDFs using vector similarity search with FAISS and then generates reliable responses using LLMs. This helps reduce hallucination and improves answer accuracy.

The system includes document loading, text chunking, embedding generation, vector database storage, semantic search, prompt engineering, and workflow management using LangGraph.

This project is useful for financial advisors, banking professionals, investment analysts, and students who need quick and trustworthy answers from complex financial documents.

## Key Features

* PDF-based financial document question answering
* Retrieval-Augmented Generation (RAG)
* FAISS vector database for fast similarity search
* LangChain for complete RAG pipeline management
* LangGraph for workflow orchestration
* OpenAI-powered intelligent response generation
* Reduced hallucination using trusted document retrieval
* Scalable and production-ready architecture

## Real-World Use Cases

* Investment report analysis
* Bank statement understanding
* Financial policy document search
* Annual report summarization
* Risk analysis support
* Financial knowledge assistant

## Tech Stack

* Python
* LangChain
* LangGraph
* FAISS
* OpenAI API
* Hugging Face Embeddings
* FastAPI
* Streamlit
* PyPDF
* Pandas

## GitHub Repository Name

Financial-RAG-Chatbot-Distributed-RAG

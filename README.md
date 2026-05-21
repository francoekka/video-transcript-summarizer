# 🎥 TranscriptIQ – RAG‑powered Summarizer & Response System

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![LangChain](https://img.shields.io/badge/langchain-0.2.6-orange.svg)
![Gradio](https://img.shields.io/badge/gradio-4.44.1-green.svg)
![FAISS](https://img.shields.io/badge/faiss-1.8.0-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

## 📌 Overview
This project is a **Retrieval-Augmented Generation (RAG) application** that processes YouTube video transcripts. It provides:
- Concise summaries of video content.
- Interactive Q&A based on transcript context.

By combining transcript retrieval, embeddings, FAISS similarity search, and LLM reasoning, the app delivers both high-level overviews and detailed answers about videos.

---

## ⚙️ Features
- Fetches transcripts directly from YouTube videos.
- Summarizes transcripts into clear, concise overviews.
- Answers user questions using context-aware retrieval.
- Uses **Gemma LLM via Ollama** for generation.
- Embedding powered by **Sentence-Transformers (MiniLM)**.
- Vector search with **FAISS**.
- Simple **Gradio UI** for interaction.

---

## 🛠️ Tech Stack
- **Python 3.11**
- **LangChain** (chains, prompts, embeddings)
- **Ollama (Gemma4:e4b)** – LLM
- **Sentence-Transformers** – embeddings
- **FAISS** – vector store
- **Gradio** – user interface
- **YouTube Transcript API** – transcript retrieval

---

## 🚀 Setup & Installation
Clone the repo and run the setup script:

```bash
git clone https://github.com/francoekka/video-transcript-summarizer.git
cd video-transcript-summarizer
bash setup.sh

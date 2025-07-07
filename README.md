# 💬 Chat Summarizer (Gradio App)

A simple web app that summarizes chat logs using a Hugging Face LLM. Paste your chat or upload a `.txt` file — get a concise summary instantly!

## ✨ Features

- 📝 Paste chat logs directly
- 📂 Upload `.txt` files with conversations
- 🧠 Summarization powered by `facebook/bart-large-cnn`
- 🌐 Clean web UI using Gradio

## 🧠 How It Works

- The app uses the transformers library with facebook/bart-large-cnn summarization pipeline.
- Long chat text is broken into manageable chunks.
- Each chunk is summarized individually, and the final result is a merged version of all partial summaries.

---

## 🚀 Getting Started

### 1. Install the dependencies
```
pip install -r requirements.txt
```

### 2. Run the app
```
python app.py
```
---

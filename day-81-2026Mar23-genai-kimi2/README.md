# 🤖 Kimi AI Chat Implementations (Moonshot AI)

This directory contains two implementations of the **Kimi AI Chat** interface using **Streamlit**. One is powered by **Groq** (Cloud Streaming) and the other by **Ollama** (Local Offline).

---

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following installed:

### 🐍 Python Dependencies
```bash
pip install streamlit groq ollama python-dotenv
```

### ☁️ Cloud Setup (Groq)
- You need a **Groq API Key**. Create one at [console.groq.com](https://console.groq.com/).
- Create a `.env` file in this directory and add your key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 🏠 Local Setup (Ollama)
- Download and install **Ollama** from [ollama.com](https://ollama.com/).
- Pull the Kimi model (Ensure you have a manifest or matching model name):
```bash
ollama run kimi-k2.5:cloud
```

---

## 🚀 How to Run

Since these are Streamlit applications, use the following commands:

### 1. Running Kimi via Groq (Cloud Stream)
```bash
streamlit run kimi-groq.py
```
- **Model**: `moonshotai/kimi-k2-instruct-0905`
- **Features**: Sub-second latency via Groq LPU, streaming responses, chat history.

### 2. Running Kimi via Ollama (Local/Offline)
```bash
streamlit run kimi-ollama.py
```
- **Model**: `kimi-k2.5:cloud`
- **Features**: Fully private/offline, streaming UI, chat memory.

---

## 📁 Directory Structure

- `kimi-groq.py`: Streamlit implementation using the Groq SDK.
- `kimi-ollama.py`: Streamlit implementation using the Ollama Python library.
- `.env`: (User Created) Stores secret API keys.
- `README.md`: This documentation.

## Claude download
- https://claude.ai/download/

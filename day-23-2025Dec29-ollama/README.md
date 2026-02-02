### OLAMA

llm -> paid, free

openai -> chatgpt

olama lets you run llm's locally

https://ollama.com/ -> Download and install ollama

models -> https://ollama.com/search -> https://ollama.com/library/gemma3 -> gemma3:270m

```bash
ollama --help

ollama ls

ollama pull gemma3:270m

ollama ls

ollama run gemma3:270m
>>> 10 points about roles and responsibility of genai developer in organization
>>> Do you have access for local path?

ollama pull deepseek-r1:1.5b

ollama run deepseek-r1:1.5b
>>> Do you have access for local path?
```

```bash
python3.12 -m venv .venv
source .venv/bin/activate

python3.12 -m pip install streamlit

python3.12 -m pip install ollama

python3.12 -m streamlit run app.py
```

# 🤖 LLM Tools & Generative AI

This section explores the practical side of using Large Language Models (LLMs), from running them locally on your own hardware to understanding the limitations of cloud-based giants like ChatGPT.

---

## 🛠️ LLM Tool Categories
Modern AI development uses a mix of local and cloud-based tools:

| Category | Tools | Cost | Best For |
| :--- | :--- | :--- | :--- |
| **Local LLM** | Ollama, LM Studio | Free (Open Source) | Privacy, Offline use, Developers |
| **Cloud LLM** | ChatGPT, Claude, Gemini | Paid (Plus) / Free (Basic) | High intelligence, Ease of use |

---

## 🏠 Local AI: Ollama.com
Ollama allows you to download and run AI models directly on your machine. However, your **Hardware is the Gatekeeper**.



### Hardware Constraints & RAM
* **The 4GB Ram Limit:** If your system has only 4GB of RAM, running larger models (like Llama 3 or Mistral) will be extremely slow or fail entirely. 
* **Model Size vs. Memory:** * A typical 7B-parameter model requires about **5.9GB - 8GB** of free memory to run smoothly.
    * **Observation:** If the application size is 5.9GB and you only have 4GB RAM, it simply won't work effectively. Your system will "swap" to the hard drive, making the response time unbearable.
* **Pro-Tip:** Always check the **Control Panel** (Windows) or **System Monitor** (Mac/Linux) to see your actual available RAM before installing a model.

---

## ⚠️ The Accuracy Reality: "Hallucinations"
A common question in the 5:30 PM Batch: **"Does ChatGPT provide wrong responses?"**
> **Answer:** Yes. Confidently and frequently.

### Why does this happen?
1. **Hallucination:** LLMs are built to predict the *next most likely word*, not to check facts against a database. They prioritize sounding natural over being accurate.
2. **Confidence over Truth:** AI often delivers incorrect information with a highly authoritative tone, making errors hard to spot.
3. **Training Cut-offs:** Models only know what was in their training data. If something happened yesterday, the model might "guess" based on old patterns.



---

## 🏗️ LLM + Generative AI Integration
In our **Agentic AI** projects, we don't just "chat." We use these models as engines:
* **LLM Model:** The "Brain" that processes language.
* **Generative AI:** The ability to create new content (Text, Code, Images).
* **Agentic AI:** Giving the model "Tools" to verify its own facts or run Python code to fix its inaccuracies.

---

## 📈 Summary of LLM Best Practices
* **Verify Everything:** Never copy-paste AI code or facts into a project without testing.
* **Optimize Local Setup:** If you have low RAM, look for "Quantized" or "Tiny" models (e.g., Phi-3 or TinyLlama) on Ollama.
* **Use RAG:** To solve inaccuracies, we use **Retrieval Augmented Generation** (RAG) to give the AI access to real, updated documents.

---

## 🚀 Final Goal
By the end of this module, you will be able to set up **Ollama** locally (hardware permitting) and connect it to a **Streamlit** UI to create your own "Local ChatGPT" that runs privately on your data.

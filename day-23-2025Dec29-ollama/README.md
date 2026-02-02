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

## LLMs and Generative AI: Tools & Models

Large Language Models (LLMs) are the engines behind modern Generative AI. While they are incredibly powerful, they require specific hardware resources and a critical eye for accuracy.

---

## 🛠️ LLM Tool Categories

### 1. Local LLMs (The "Free & Private" Way)

**Ollama** is the leading tool for running AI models directly on your own computer.

* **Website:** [ollama.com](https://ollama.com)
* **Hardware Requirements:**
* **RAM:** This is the most critical factor. If your system has only **4GB of RAM**, most models will be extremely slow or fail to run.
* **Application Size:** A standard model (like Llama 3) often takes about **5GB to 6GB** of space.
* **Tip:** Always check your "Installed Apps" in the Control Panel to manage your disk space.



### 2. Cloud-Based LLMs (Paid vs. Free)

* **Free Tier:** ChatGPT (GPT-4o mini), Google Gemini, and Claude (Sonnet). These are great for general tasks but have usage limits.
* **Paid Tier:** ChatGPT Plus, Claude Pro, and Gemini Advanced. These provide access to more "reasoning" power, higher limits, and advanced features like data analysis.

---

## ⚠️ The Accuracy Challenge: Why LLMs Fail

You asked: *Does ChatGPT provide wrong and inaccurate responses?*
**Yes.** This is a documented phenomenon known as **Hallucination.**

* **Reason:** LLMs are "probabilistic," not "deterministic." They predict the next most likely word in a sentence based on patterns, not necessarily based on facts.
* **Risks:** They can confidently state false dates, invent non-existent Python libraries, or solve math problems incorrectly.
* **Solution:** Always use the **"Human-in-the-Loop"** approach. Never copy-paste code or facts without verifying them.

---

## 🧠 Generative AI vs. LLM Models

Understanding the hierarchy helps you choose the right tool for the job.

* **Generative AI:** The broad umbrella. It includes everything that *creates* content (Text, Images, Video, Audio).
* **LLM (Large Language Model):** The specific type of AI trained on text to understand and generate human language.
* **LMM (Large Multimodal Model):** Modern models that can "see" images and "hear" audio in addition to text.

---

For your **IPL Data Analysis project**, use LLMs as a **Coding Assistant**, not a **Data Analyst**:

1. **Do:** Ask the LLM to explain a complex `**kwargs` function or help with a Matplotlib error.
2. **Don't:** Ask the LLM to "Tell me who won the 2024 IPL" without checking, as its training data might be outdated.


- fine tuning - making the model to run locally

- https://chat.deepseek.com/

```bash
ollama pull deepseek-r1:1.5b

ollama run deepseek-r1:1.5b
```

## Difference between `deepseek-1.py` and `deepseek-2.py`

**1. `deepseek-1.py` (Direct Ollama API):**
- Uses the official `ollama` Python package to communicate directly with the local Ollama server (`localhost:11434`).
- Provides a straightforward UI where the user enters text in a `st.text_area` and manually clicks a "Generate Response" button to trigger the execution (which includes a loading spinner).

**2. `deepseek-2.py` (LangChain Integration):**
- Uses the `langchain-ollama` integration to connect the model into a LangChain Expression Language (LCEL) pipeline (`chain = prompt | model`).
- This approach is highly modular, making it much easier to add memory, parsing tools, or vector database components in the future to build a sophisticated Agentic AI.
- The UI execution triggers immediately upon user submission in the `st.text_input`, skipping the need for a physical "Generate" button.

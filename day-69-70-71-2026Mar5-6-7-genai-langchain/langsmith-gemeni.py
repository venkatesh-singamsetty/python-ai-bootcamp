import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ==============================
# 🔐 API KEYS & LANGSMITH SETUP
# ==============================
# Ensure API keys are set from environment variables (sourcing setup-secrets.sh is recommended)
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = "venky-langsmith-project"

# ==============================
# 🧠 Prompt Template
# ==============================
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are Gemini Flash — a fast, multimodal, and intelligent AI assistant. Please respond clearly and helpfully."),
        ("user", "Question: {question}")
    ]
)

# ==============================
# ⚙️ Streamlit UI
# ==============================
st.title("🤖 GEMINI FLASH CHATBOT - POWERED BY LANGSMITH ")
input_text = st.text_input("💬 Ask me anything:")

# ==============================
# 🌟 Gemini Model Setup
# ==============================
# Using gemini-2.5-flash or if supported in your region
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.2,
    max_output_tokens=1024
)

# Output parser for string responses
output_parser = StrOutputParser()

# Combine into LCEL chain
chain = prompt | llm | output_parser

# ==============================
# 💬 Handle User Input
# ==============================
if input_text:
    with st.spinner("🤔 Gemini is generating a response..."):
        try:
            response = chain.invoke({"question": input_text})
            # Apply the requested newline formatting
            formatted_response = response.replace('\n\n', '\n')
            
            st.success("✅ Here's my response:")
            st.write(formatted_response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
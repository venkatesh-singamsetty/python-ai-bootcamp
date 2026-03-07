from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

# Ensure API keys are set from environment
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "OPENAI-GPT-PROJECT")

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "I am chatbot. I am here to assist you. Please type your queries"),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title('LLM-OPENAI PROJECT - CUSTOM GPT-4 BY PRAKASH SENAPATI')
input_text = st.text_input("How may I help you")

# OpenAI LLM - 'gpt-4o-mini' is a valid, fast model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({'question': input_text})
    # Replace double newlines with single ones as requested
    st.write(response.replace('\n\n', '\n'))

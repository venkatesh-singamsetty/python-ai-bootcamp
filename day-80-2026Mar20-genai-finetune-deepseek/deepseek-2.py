from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
# Set the app title
st.title("Venky bot using DeepSeek-R1")
# Define the prompt template
template = """Question: {question}
Answer: Let's think step by step."""
# Create the prompt template using the given template
prompt = ChatPromptTemplate.from_template(template)
# Initialize the model (uncomment the correct model depending on your choice)
# model = OllamaLLM(model="llama3.1")
model = OllamaLLM(model="deepseek-r1:1.5b") 
# Create a chain with the prompt and the model
chain = prompt | model
# Use text_input to capture user question
question = st.text_input("Enter your question here")
# If the user has entered a question, format the prompt and invoke the chain
if question:
    try:
        # Since we are using a chain (prompt | model), 
        # we can just pass a dictionary with the input variables to the chain!
        response = chain.invoke({"question": question})
        
        # Display the response from the model
        st.write(response)
    except Exception as e:
        st.write(f"Error: {e}")
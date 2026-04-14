# pip install streamlit anthropic python-dotenv

import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Validate API key
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    st.error("ANTHROPIC_API_KEY not found. Please set it in your .env file.")
    st.stop()

# Initialize Claude client
client = anthropic.Anthropic(api_key=api_key)

# Streamlit UI config
st.set_page_config(page_title="Claude AI Chatbot", page_icon="🤖")
st.title("🤖 Claude AI Chatbot")
st.write("Built with Anthropic Claude")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare messages for Claude
    claude_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    # Call Claude API (temperature removed — not supported in this SDK usage)
    response = client.messages.create(
        model="claude-sonnet-4-5",  # pinned stable model
        max_tokens=1024,
        messages=claude_messages
    )

    answer = response.content[0].text

    # Store and display assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
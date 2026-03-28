import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

# Page config
st.set_page_config(
    page_title="Kimi AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Kimi (Moonshot) AI Chat")
st.caption("Groq Streaming • Kimi K2")

# Init Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Ask something...")

if prompt:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        stream = client.chat.completions.create(
            model="moonshotai/kimi-k2-instruct-0905",
            messages=st.session_state.messages,
            temperature=0.6,
            max_completion_tokens=2048,
            stream=True
        )

        for chunk in stream:
            # 🔑 SAFE extraction
            if (
                chunk.choices
                and chunk.choices[0].delta
                and chunk.choices[0].delta.content
            ):
                token = chunk.choices[0].delta.content
                full_response += token
                placeholder.markdown(full_response)

        # Fallback (VERY IMPORTANT)
        if full_response.strip() == "":
            full_response = "⚠️ No response generated. Please try again."

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )

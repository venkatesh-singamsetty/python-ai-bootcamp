import streamlit as st
import os
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown
#from altair.vegalite.v4.api import Chart
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
import os
import google.generativeai as genai
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)
## Function to load gemini model and get respones
def get_gemini_response(question):
    model = genai.GenerativeModel('models/gemini-3-flash-preview')
    #model = genai.GenerativeModel('gemini-2.5-flash-preview-04-17')
    response = model.generate_content(question)
    return response.text
##initialize our streamlit app
st.set_page_config(page_title="GEMINI LLM APP")
st.header("Gemini AI BOT Application")
input=st.text_input("Input: ",key="input")
submit=st.button("click me to generate response")
## If ask button is clicked
if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)

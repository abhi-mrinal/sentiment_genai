import streamlit as st
from model_api import createModel , generate_response
from prompts import prompt1 , prompt2

st.title("Sentiment Analysis using Gemini")
api_key = st.text_input(value = None , label = "YOUR GEMINI API KEY" , type = "password")
if api_key:
    llm = createModel(api_key)
with st.form("my_form"):
    text = st.text_area(
        "Enter the review to know its sentiment"
    )
    finalPrompt1 = prompt1.format(rev = text)
    finalPrompt2 = prompt2.format(rev = text)
    submitted = st.form_submit_button("Submit")
    if submitted:
        x = generate_response(llm , finalPrompt1)
        y = generate_response(llm , finalPrompt2)
        st.write(x)
        st.write(y)


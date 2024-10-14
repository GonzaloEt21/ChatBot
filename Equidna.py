#python -m streamlit run C:\Users\ManciniPereyra\Desktop\escritorio\PY\Equidna.py
#KEy Groq ( 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 )


import streamlit as st
import groq as gq

st.set_page_config(page_title="Equidna IA")

with st.sidebar:
    groq_api_key = st.text_input("Chat")

st.title("Habla con Equidna")

st.chat_input("Comentale a Equidna que deseas")
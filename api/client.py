import requests
import streamlit as st

# def get_openai_response(input_text):
#     response = requests.post("http://localhost:8000/essay/invoke", json={"input":{'topic':input_text}})
#     return response.json()['output']['content']

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={"input": {'topic': input_text}})
    if response.status_code == 200:
        return response.json()['output']['content']
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None


def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={"input":{'topic':input_text}})
    return response.json()['output']

st.title("Langchain with OpenAI and LLAMA3.2 API")
input_text1 = st.text_input("Write an eassy on")
input_text2 = st.text_input("Write a poem on")

if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
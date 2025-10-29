import streamlit as st
import requests

def generat_ai_response(prompt:str) -> str:
    url = "https://cent.ischool-iot.net/api/genai/generate"
    data = {"query": prompt}
    headers = {'x-api-key':'0d3f7b655de69798a60aad9a'}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()

st.title("Frst GPT API call")
prompt = st.text_area("Enter your prompt here:")
if st.button("Generate Response"):
    try:
        ai_response = generat_ai_response(prompt)
        st.subheader("AI Response:")
        st.write(ai_response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
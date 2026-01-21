import streamlit as st
import requests

st.title("RAG Modernization Platform")

q = st.text_input("Ask a question about the codebase")

if q:
    try:
        res = requests.post(
            "http://localhost:8000/query/",
            json={"question": q},
            timeout=5
        )

        if res.status_code != 200:
            st.error(res.text)
        else:
            st.json(res.json())

    except Exception as e:
        st.error(str(e))

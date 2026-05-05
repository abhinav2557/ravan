import streamlit as st
from groq import Groq

client = Groq(api_key="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")

st.title("ravan")

user_input = st.text_input("Ask anything:")

if user_input:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)
import streamlit as st
from groq import Groq
import os
import urllib.parse

st.set_page_config(page_title="Ravan AI", page_icon="🤖", layout="wide")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are Ravan AI, a smart, helpful conversational assistant.
Answer clearly and naturally.
Help with coding, studies, and practical tasks.
"""

st.title("🤖 Ravan AI")
st.caption("Chat + Image Generator")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def generate_image(prompt):
    encoded_prompt = urllib.parse.quote(prompt)
    return f"https://image.pollinations.ai/prompt/{encoded_prompt}"

st.subheader("🎨 Image Generator")
image_prompt = st.text_input("Enter image prompt")
generate_btn = st.button("Generate Image")

prompt = st.chat_input("Ask me anything...")

if generate_btn and image_prompt:
    st.subheader("Generated Image")
    img = generate_image(image_prompt)
    st.image(img, use_container_width=True)

if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

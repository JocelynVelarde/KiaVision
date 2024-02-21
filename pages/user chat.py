import streamlit as st
from assistant_openai import ask_gpt
from vision_openai import analyze_image

st.title("Vision out 💡")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    result = analyze_image(uploaded_file)
    with st.chat_message("assistant"):
        st.markdown(result)


if prompt := st.chat_input("Tell me your problem or upload an image to get started! 📸"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = ask_gpt(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    
# Usage:
with open("assets/images/flowera.jpg", "rb") as image_file:
    result = analyze_image(image_file)
    print(result)

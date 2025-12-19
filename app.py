import streamlit as st

st.set_page_config(page_title="Simple Chatbot")

st.title("🤖 Simple Python Chatbot")

st.markdown(
    "**Disclaimer:** This chatbot is for educational purposes only."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

def chatbot_response(text):
    text = text.lower()

    if "hi" in text or "hello" in text:
        return "Hello! How can I help you?"
    elif "how are you" in text or "how are u" in text:
        return "I am fine, thank you!"
    elif "your name" in text:
        return "I am a simple Python chatbot."
    elif "bye" in text:
        return "Goodbye! Have a nice day 😊"
    else:
        return "Sorry, I didn't understand that."

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = chatbot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)


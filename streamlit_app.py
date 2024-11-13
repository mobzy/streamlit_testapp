import streamlit as st
from streamlit_chat import message  # This will allow easy chat display within Streamlit

# Title and intro
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("AI Chatbot Application")
st.write("Welcome to the AI Chatbot! Please enter your API key to start chatting.")

# Store the API key securely in the session state
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

# API Key input section
if not st.session_state["api_key"]:
    st.session_state["api_key"] = st.text_input("Enter your API key to proceed:", type="password")
    if st.session_state["api_key"]:
        st.success("API key entered successfully! You can start chatting.")
    else:
        st.warning("Please enter your API key to start the conversation.")

# Initialize the chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Chat input and response section
if st.session_state["api_key"]:
    user_input = st.text_input("You:", "")
    if user_input:
        # Placeholder AI response (since we're using only Streamlit)
        ai_response = f"AI Response to: {user_input}"

        # Store the interaction in chat history
        st.session_state["chat_history"].append((user_input, ai_response))
        
        # Clear the input box for next message
        st.empty()

    # Display chat history
    st.write("### Chat History")
    for i, (user_query, bot_response) in enumerate(st.session_state["chat_history"]):
        message(user_query, is_user=True, key=f"{i}_user")
        message(bot_response, key=f"{i}_bot")

# If no API key is present, hide chat input to prevent interaction
else:
    st.info("Please enter your API key to start using the chatbot.")

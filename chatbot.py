import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
model = 'gpt-3.5-turbo'

# Configure the Streamlit page
st.set_page_config(page_title='Chat Bot', page_icon='🤖', layout='wide')

# Set the title of the Streamlit app
st.title("Chat Bot - powered by GPT 3.5")

# Initialize chat history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to process user input and generate response
def llm_function(query):

    # Add user message to chat history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Use OpenAI's API to generate response
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(model=model, messages=st.session_state.messages)

    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(response.choices[0].message["content"])

    # Add assistant's response to chat history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.choices[0].message["content"]
        }
    )

# Accept user input
query = st.chat_input("Please enter your question here")

# Call the function when input is provided
if query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(query)

import ollama
import streamlit as st

model = 'qwen2:0.5b-instruct'

st.title('pi LLM')
st.logo('images/raspberry-pi.svg')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Enter Your Prompt Here")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare the assistant's response container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Stream the response from the model
        response_stream = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True  # Enable streaming
        )

        for response_chunk in response_stream:
            token = response_chunk['message']['content']
            full_response += token
            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

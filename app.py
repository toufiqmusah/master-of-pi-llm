import ollama
import streamlit as st

model = 'qwen2:0.5b-instruct'

st.title('My pi LLM')

prompt = st.chat_input("Enter Your Prompt Here")

response_stream = ollama.chat(model = model, 
							  messages = [
								{
									'role':'user',
									'content':prompt,
								
								}],)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

response = response_stream['message']['content']
# Display assistant response in chat message container
with st.chat_message("assistant"):
    st.markdown(response) 
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
#print(response_stream['message']['content'])
How to Install and run a personal llm on a raspberry pi

Requirements
- A raspberry pi 4
- Ollama installed

For this tutorial, we will be using the ollama library and its repository of models.

Step 1:
Download and install ollama through the cli through the following command:
'curl -fsSL https://ollama.com/install.sh | sh'

Step 2: 
Pick a specific ollama model to use for your use case from the ollama repository.
For my use case, I am using the microsoft phi-3 model for its high performane and optimised size.

'ollama run phi3:3.8b'

Other model options suitable for the raspberry pi include:
- qwen2:0.5b-instruct
- llama3.1:8b
- gemma2:2b
- mistral:7b

After running the above command, the selected model will be downloaded and accessible locally.

Step 3:
Up next is writing a python app that will serve as the front-end. For this endeavour, we will use streamlit.

First of all, in the cli create a virtual environment:
'python -m venv my-env'

Activate the virtual environment
'source my-env/bin/activate'

Install streamlit on your system with the following command in the environment:

'pip install streamlit'

Create a new directory, and in it, create a python file and name it.
Mine is the llm-app.python

Open llm-app.py in your IDE and write the following code for accessing and running your llm locally:

%------------%

import ollama
import streamlit as st



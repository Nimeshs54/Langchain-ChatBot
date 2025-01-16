# Chatbot Apps using Langchain

This repository contains two chatbot applications built using Langchain—one powered by OpenAI GPT-3.5 and the other by Ollama Llama-3.2. These apps demonstrate how to integrate different LLMs (Large Language Models) with a simple user interface using Streamlit.

## 🚀 Features

- **OpenAI GPT-3.5 Chatbot**: Leverages OpenAI's GPT-3.5 model to answer queries.
- **LLama Chatbot (via Ollama)**: Leverages the Ollama API to interact with the Llama model (Llama-3.2).
- **Custom Prompt Templates**: Each chatbot uses a specific prompt template to ensure effective responses.
- **Streamlit UI**: Provides an interactive user interface for easy testing and usage.
- **Environment Setup**: API keys and configurations are managed using a `.env` file.

## 🛠️ Technologies Used

- **Langchain**: A framework for developing chatbots and LLM-based applications.
- **OpenAI GPT-3.5**: A state-of-the-art language model by OpenAI.
- **Ollama**: A platform for using the Llama model (Llama-3.2).
- **Streamlit**: A framework for building interactive web apps for data science and machine learning.
- **dotenv**: For managing environment variables securely.

- ## 💡 How It Works

### **1. OpenAI GPT-3.5 Chatbot (app.py)**

This app uses the OpenAI GPT-3.5 model via Langchain's `ChatOpenAI` class to process user queries. The response is then displayed on a simple Streamlit interface. It’s perfect for creating Q&A-based chatbot applications using OpenAI's models.

### **2. Llama Chatbot (locallama.py)**

This app uses the **Llama-3.2** model through the Ollama API. It's designed to interact with Llama using Langchain's `Ollama` class. It supports the same Streamlit-based interface, making it easy to test out queries with the Llama model.

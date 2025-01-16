from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A server for LangChain",
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
llm1 = ChatOpenAI()
llm2 = Ollama(model="llama3.2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 30 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 30 words")

add_routes(
    app,
    prompt1|llm1,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm2,
    path="/poem"
)


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)
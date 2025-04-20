from fastapi import FastAPI
from dotenv import load_dotenv
from langserve import add_routes
import uvicorn
import os

from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
model=ChatOpenAI()


##ollama llama3.2:3b
llm=Ollama(model="llama3.2:3b")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"


)

add_routes(
    app,
    prompt2|llm,
    path="/poem"


)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)

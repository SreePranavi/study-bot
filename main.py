import os
import certifi
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pymongo import MongoClient
from datetime import datetime


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
mongo_uri = os.getenv("MONGODB_URI")


client = MongoClient(
    mongo_uri,
    tls=True,
    tlsCAFile=certifi.where()
)
db = client["studybot"]
collection = db["chats"]


app = FastAPI()


llm = ChatGroq(
    api_key=groq_api_key,
    model="openai/gpt-oss-20b"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         "You are an AI Study Assistant. Answer academic and learning-related questions clearly and simply. "
         "Use examples when needed."),
        ("placeholder", "{history}"),
        ("user", "{question}")
    ]
)

chain = prompt | llm


class ChatRequest(BaseModel):
    user_id: str
    question: str


def get_history(user_id):
    chats = collection.find({"user_id": user_id}).sort("timestamp", 1)
    history = []
    for chat in chats:
        history.append((chat["role"], chat["message"]))
    return history


@app.post("/chat")
def chat(request: ChatRequest):
    history = get_history(request.user_id)

    response = chain.invoke({
        "history": history,
        "question": request.question
    })

    
    collection.insert_one({
        "user_id": request.user_id,
        "role": "user",
        "message": request.question,
        "timestamp": datetime.utcnow()
    })

    
    collection.insert_one({
        "user_id": request.user_id,
        "role": "assistant",
        "message": response.content,
        "timestamp": datetime.utcnow()
    })

    return {"response": response.content}
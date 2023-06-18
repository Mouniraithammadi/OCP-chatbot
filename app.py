from fastapi import FastAPI
from main import  getReply
app = FastAPI()
# from main import chat
# define your chat function here
def chat(q: str, dictt: dict) -> str:
    # your implementation here
    return "Hello, you said: " + q

@app.post("/chatbot")
async def chatbot_endpoint(q: str, dictt: dict):
    response = getReply(q, dictt)
    return {"response": response}

from fastapi import APIRouter
from controller.chatbot import chatbot_response

chatbot = APIRouter()

@chatbot.post('/chatbot')
async def chat_bot(text: str):
    return chatbot_response(text)



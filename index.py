from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.favourite import favourite
from routes.activity import activity
from routes.google_map import place
from routes.chatbot import chatbot
# from routes.booking import booking

app = FastAPI()

previous_val = "None"

origins = [
    "exp://192.168.1.2:19000",
    "http://192.168.1.2:19000"
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.0.100:19006",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(place)
app.include_router(favourite)
app.include_router(activity)
app.include_router(chatbot)
# app.include_router(booking)
print("<============== Server started ==============>")


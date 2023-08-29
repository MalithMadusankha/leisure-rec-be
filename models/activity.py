from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Activity(BaseModel):
    name: str
    address: str
    type: List[str]
    photo_ref: List[str]
    lat: int
    lng: int
    rating: int
    time: str
    date: str
    about: str
    place_id: str
    _id: str
    
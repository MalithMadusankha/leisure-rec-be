from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Favourite(BaseModel):
    name: str
    address: str
    type: List[str]
    leisure_type: List[str]
    photo_ref: List[str]
    lat: int
    lng: int
    rating: int
    place_id: str
    _id: str
    
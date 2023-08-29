from fastapi import APIRouter
from controller.favourite import create, getOne, getAll, update, delete
from models.favourite import Favourite

favourite = APIRouter()

@favourite.post('/favourite')
async def create_favourite(favourite: Favourite):
    res = create(favourite)
    print("res : ", res)
    return res

@favourite.get('/favourite/{favourite_id}')
async def get_favourite_by_id(favourite_id: str):
    favourite = getOne(favourite_id)
    if favourite:
        return favourite
    return {"message": "Favourite not found"}

@favourite.delete('/favourite/{favourite_id}')
async def delete_favourite(favourite_id: str):
    return delete(favourite_id)

@favourite.get('/favourites')
async def get_all_favourites():
    favourites = getAll()
    return favourites

@favourite.put('/favourite/{favourite_id}')
async def update_favourite_by_id(favourite_id: str, updated_favourite: Favourite):
    updated_favourite = update(favourite_id, updated_favourite)
    if updated_favourite:
        return updated_favourite
    return {"message": "Favourite not found"}

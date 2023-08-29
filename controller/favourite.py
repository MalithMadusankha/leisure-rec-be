from fastapi import HTTPException
from typing import List, Dict
from models.favourite import Favourite
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(favourite: Favourite):
    print("<===== Create Favourite =====>")
    inserted_result = db.favourite.insert_one(dict(favourite))
    inserted_favourite = db.favourite.find_one({"_id": inserted_result.inserted_id})
    return serializeDict(inserted_favourite)
    
def getAll():
    print("<===== Get All Favourite =====>")
    return serializeList(db.favourite.find())


def getOne(id):
    print("<===== getLastOne =====>")
    res = serializeDict(db.favourite.find_one({"_id": ObjectId(id)}))
    print(res)
    return res

def update(id, favourite: Favourite):
    db.favourite.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(favourite)
    })
    inserted_doc = db.favourite.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Favourite =====>", id)
    result = db.favourite.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Favourite not found")
    return {"status_code": 200, "detail": "Favourite Deleted" }
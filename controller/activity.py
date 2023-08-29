from fastapi import HTTPException
from typing import List, Dict
from models.activity import Activity
from schemas.serialize import serializeDict, serializeList
from config.db import db
from bson import ObjectId

def create(activity: Activity):
    print("<===== Create Activity =====>")
    db.activity.insert_one(dict(activity))
    
def getAll():
    print("<===== Get All Activity =====>")
    return serializeList(db.activity.find())

def getOne(id):
    print("<===== getOne =====>")
    res = serializeDict(db.activity.find_one({"_id": ObjectId(id)}))
    print(res)
    return res

def update(id, activity: Activity):
    db.activity.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(activity)
    })
    inserted_doc = db.activity.find_one({"_id": ObjectId(id)})
    return serializeDict(inserted_doc)

def delete(id: str):
    print("<===== delete Activity =====>", id)
    result = db.activity.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Activity not found")
    return {"status_code": 200, "detail": "Activity Deleted" }

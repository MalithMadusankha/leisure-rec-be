from fastapi import APIRouter
from controller.activity import create, getOne, getAll, update
from models.activity import Activity

activity = APIRouter()

@activity.post('/activity')
async def create(activity: Activity):
    res = create(activity)
    print("res : ", res)
    return res

@activity.get('/activity/{id}')
async def get_by_id(id: str):
    activity = getOne(id)
    if activity:
        return activity
    return {"message": "Activity not found"}

@activity.put('/activity/{id}')
async def update_by_id(id: str, activity: Activity):
    activity_db = update(id, activity)
    if activity_db:
        return activity_db
    return {"message": "Activity not found"}

@activity.get('/activity')
async def get_all():
    activitys = getAll()
    return activitys
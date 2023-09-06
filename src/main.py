import json
import random
import os

from typing import List
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

from src.models.Human import Human
    
## MONGODB CONNECTION ##
# MongoDB Params
mongodb_uri = os.getenv('MONGODB_URI') 

# Mongo Client
client = MongoClient(mongodb_uri)
db = client.get_database('gaia-dev')

# Init
app = FastAPI()

## ENDPOINTS ##
# Post Human
@app.post("/humans")
async def post_human(human: Human):
    result = db.humans.insert_one(human.dict())
    return {"message": "Human created successfully", "human_id": str(result.inserted_id)}

# Get Human by id
@app.get("/humans/{human_id}", response_model=Human)
async def get_human_by_id(human_id: str):
    human_data = db['humans'].find_one({"_id": human_id})
    if human_data:
        return Human(**human_data)
    else:
        raise HTTPException(status_code=404, detail="Human not found")

# Get All humans
@app.get("/humans", response_model=List[Human])
async def get_all_humans():
    humans = []
    cursor = db['humans'].find()
    for human_data in cursor:
        human = Human(**human_data)
        humans.append(human)
    return humans
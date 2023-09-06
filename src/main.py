from fastapi import FastAPI
from azure.cosmos import CosmosClient, exceptions
import json
import random
import os
    
## COSMODB CONNECTION ##
# CosmoDB Params
endpoint = os.environ.get("COSMODB_URI")
key = os.environ.get("COSMODB_KEY")
database_name = os.environ.get("COSMODB_NAME")
container_name = os.environ.get("COSMODB_CONTAINER")

# Cosmo Client
client = CosmosClient(endpoint, key)

# Obtains BDD or creates it
try:
    database = client.get_database_client(database_name)
except exceptions.CosmosResourceNotFoundError:
    database = client.create_database_if_not_exists(database_name)
    
try:
    container = database.get_container_client(container_name)
except exceptions.CosmosResourceNotFoundError:
    container = database.create_container_if_not_exists(id=container_name)

# Init
app = FastAPI()

## ENDPOINTS ##
# Post Human
@app.post("/humans")
async def post_human(data: dict):
    response = container.create_item(body=data)
    return {"message": "Human Post success", "item_id": response["id"]}

@app.post("/hello")
async def post_human(data: dict):
    return {"message": "Hello world!"}

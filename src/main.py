from fastapi import FastAPI
from azure.cosmos import CosmosClient, exceptions
import json
import random
    
## COSMODB CONNECTION ##
# CosmoDB Params
endpoint = ""
key = ""
database_name = ""
container_name = ""

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

# Post Random Human
@app.post("/humans/random")
async def post_human():
    with open('resources/stats.json') as statsJson:
        stats = json.load(statsJson)

    data = {
        "name": random.choice(stats['human']['names']),
        "lastName": random.choice(stats['human']['lastNames']),
        "physical": random.choice(stats['human']['physical']),
        "studies": random.choice(stats['human']['studies'])
    }

    response = container.create_item(body=data)
    return {"message": "Datos insertados en Cosmos DB", "item_id": response["id"]}

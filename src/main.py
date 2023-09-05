from fastapi import FastAPI
import json
import random

from models.Human import Human

with open('resources/stats.json') as statsJson:
    stats = json.load(statsJson)

name = random.choice(stats['human']['names'])
lastName = random.choice(stats['human']['lastNames'])
physical = random.choice(stats['human']['physical'])
studies = random.choice(stats['human']['studies'])

human = Human(name, lastName, physical, studies)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
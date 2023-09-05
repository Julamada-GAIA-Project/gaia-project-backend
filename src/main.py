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

if __name__ == '__main__':
    print(human)
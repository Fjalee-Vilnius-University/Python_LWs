import pymongo
from pymongo import MongoClient
import json

DATA_JSON_PATH = 'retaurants.json'

cluster = MongoClient('mongodb+srv://sa:sa@cluster0.n9p5p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster["lw2"]
collection = db["lw2"]

data = []
with open(DATA_JSON_PATH) as f:
    for line in f:
        data.append(json.loads(line))

data

collection.insert_many(data)
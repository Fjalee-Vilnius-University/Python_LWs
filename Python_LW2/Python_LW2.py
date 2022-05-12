import pymongo
from pymongo import MongoClient
import json
import sys
import os

DATA_JSON_PATH = os.path.join(sys.path[0], 'retaurants.json')

def loadDataIntoDB(collection):
    data = []
    with open(DATA_JSON_PATH) as f:
        for line in f:
            data.append(json.loads(line))

    data
    collection.insert_many(data)

def getDbCollection():
    cluster = MongoClient('mongodb+srv://sa:sa@cluster0.n9p5p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = cluster["lw2"]
    return db["lw2"]


collection = getDbCollection()
loadDataIntoDB(collection)
print("yes")


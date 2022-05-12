import pymongo
from pymongo import MongoClient
import json
import sys
import os

DATA_JSON_PATH = os.path.join(sys.path[0], 'retaurants.json')

def load_data_into_db(collection):
    data = []
    with open(DATA_JSON_PATH) as f:
        for line in f:
            data.append(json.loads(line))

    data
    collection.insert_many(data)

def get_db_collection():
    cluster = MongoClient('mongodb+srv://sa:sa@cluster0.n9p5p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = cluster["lw2"]
    return db["lw2"]

def print_query(query):
    for line in query:
        print(line)

def query_all(collection):
    query = {
        "restaurant_id": {
            "$regex": '.*?',
        }
    }
    return collection.find(query)

collection = get_db_collection()
# load_data_into_db(collection)

print_query(query_all(collection))
print_query(query_all(collection))


#       Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)
#       Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
# Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
# Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams
# Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
# Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.
# Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
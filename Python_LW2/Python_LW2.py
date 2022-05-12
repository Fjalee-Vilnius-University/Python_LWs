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

def print_one_from_query(query):
    for line in query:
        print(line)
        break

def query_all(collection):
    query = {
        "restaurant_id": {
            "$regex": '.*?',
        }
    }
    return collection.find(query)

def query_task3(collection):
    q_from = {
        "restaurant_id": {
            "$regex": '.*?',
        }
    }
    q_select = {
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1
    }
    return collection.find(q_from, q_select)

def query_task4(collection):
    q_from = {
        "restaurant_id": {
            "$regex": '.*?',
        }
    }
    q_select = {
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1,
        "_id": 0
    }
    return collection.find(q_from, q_select)

def query_task5(collection):
    q_from = {
        "borough": "Bronx"
    }
    q_select = {
        "restaurant_id": 1,
        "name": 1,
        "borough": 1,
        "cuisine": 1,
        "_id": 0
    }
    return collection.find(q_from, q_select)

collection = get_db_collection()

# load_data_into_db(collection)

# print_one_from_query(query_all(collection))
# print_one_from_query(query_task3(collection))
# print_one_from_query(query_task4(collection))
print_one_from_query(query_task5(collection))



#       1.Sukurkite restoranų duomenų rinkinį (pridedamas zip failas)
#       2.Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
#       3.Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
#       4.Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams
# 5.Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
# 6.Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.
# 7.Parašykite užklausą, kad cuisine būtų išdėstyta didėjimo tvarka, o borough - mažėjimo.
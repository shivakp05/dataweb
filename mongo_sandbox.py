from pymongo import MongoClient

import json
with open("/home/shivakp/kent/dataweb/private.json","r") as f:
    private = json.load(f)

password = private["mongo"]
client = MongoClient(f"mongodb+srv://shiva9596:{password}@soliton0.att3pbv.mongodb.net/?retryWrites=true&w=majority")

from bson.objectid import ObjectId

shopping_db = client.shopping_db
list_collection = shopping_db.list_collection

list_collection.delete_many({})

list_collection.insert_many([
        { "description": 'apples' },
        { "description": 'broccoli' },
        { "description": 'pizza' },
        { "description": 'tangerine' },
        { "description": 'potatoes' }
    ])

items = list(list_collection.find())
print(items)
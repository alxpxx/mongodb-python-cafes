from pymongo import MongoClient
from bson.objectid import ObjectId

import os

"""
You can run this program with an evironment variable using

$ export MONGO_URI=mongodb+srv://jwhol:<my-password>@cluster0-gyfz1.mongodb.net/test?retryWrites=true&w=majority
$ python3 mongo-cafe.py

This is much the same as we did with the Flask app, and when you use this database with a flask app you will also still need to use this environment variable.

Also read into https://pypi.org/project/python-dotenv/ if this feels like a tedious way to do stuff but ONLY IF YOU .gitignore YOUR .env!!!
"""
MONGO_URI = os.environ['MONGO_URI']

print("Connecting to database...")

# Connecting to the database using the environment variable.
client = MongoClient(MONGO_URI)
db = client.test

# Uses the database python-mongo-cafes, or creates it if it does not exist.
db = client["python-mongo-cafes"]

cafe = {
        "name": "Charlie and Franks",
        "coffee": "Good",
        "employees": 16
        }
cafes = db.cafes

print("Adding new cafe...")

# Inserts the cafe and records the ID that was assigned to it
cafe_id = cafes.insert_one(cafe).inserted_id
print("Cafe id: \n", cafe_id, "\n")

# The single cafe we added.
foundCafe = cafes.find_one({"coffee":"Good"})
print("The cafe we added: \n", foundCafe, "\n")

# Update a cafes employees
print('changing employees to 20...\n')
cafes.update_one({'_id': cafe_id}, {'$set': {'employees': 20}})

# A list of all cafes in the cafes collection.
allCafes = list(cafes.find())
print("The whole list of cafes: \n", allCafes, "\n")

input("Go see if the document is on the database, then press enter to continue...\n")
print("Deleting Cafe")

cafes.delete_one({
    "name":"Charlie and Franks"
    })

print(db.list_collection_names())
print("Done")


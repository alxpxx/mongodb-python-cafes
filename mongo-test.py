from pymongo import MongoClient
import os

MONGO_URI = os.environ['MONGO_URI']

print("Connecting to database...")

client = MongoClient(MONGO_URI)
db = client.test

db = client["python-mongo-cafes"]

cafe = {
        "name": "Charlie and Franks",
        "Coffee": "Good",
        "Employees": 16
        }

cafes = db.cafes


print("Adding new cafe...")
cafe_id = cafes.insert_one(cafe).inserted_id
print(cafe_id)

foundCafe = cafes.find_one({"Coffee":"Good"})
print(foundCafe)

input("Go see if the document is on the database, then press enter to continue...")
print("Deleting Cafe")

cafes.delete_one({
    "name":"Charlie and Franks"
    })

print(db.list_collection_names())


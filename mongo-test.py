from pymongo import MongoClient
import os

DB_USERNAME = os.environ['DB_USERNAME']
DB_PASSWORD = os.environ['DB_PASSWORD']

print("Connecting to database...")
client = MongoClient(f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@ds331568.mlab.com:31568/python-mongo-test?retryWrites=false')
db = client["python-mongo-test"]

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


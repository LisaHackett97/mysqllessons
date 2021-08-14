import os
import pymongo
if os.path.exists("env.py"):
    import env

# Set Constant Variables
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDatabase"
COLLECTION = "celebrities"

# function to connect to DB
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

# Calling the connection function. Passing it the hidden MONGO_URI Var as the url arg
conn = mongo_connect(MONGO_URI)

# set collection name
coll = conn[DATABASE][COLLECTION]

coll.remove({"first": "douglas"})
coll.update_one({"nationality": "american"}, {"$set": {"hair_color": "maroon"}})


# This will return a MongoDB object, also called a cursor, 
# which then need to iterate over.

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)
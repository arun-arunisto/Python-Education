# to install pymongo use the below cmd
"""
pip install 'pymongo[srv]'
"""
import datetime

from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId
import pprint

load_dotenv()

# the connection string i loaded on .env and it accessed using os
MONGODB_URI = os.getenv("MONGODB_URI")

#connecting to mongodb client using above string
client = MongoClient(MONGODB_URI)

#printing all database names inside the cluster
#the below code print database names inside a cluster on a form of list
#print("Databases:\n",client.list_database_names())

#geting refrence to database
db = client.test

#getting refrence to collection
test_collec = db.test_collection


#adding data inside a collection
"""
sample_data = {
    "name":"arun arunisto",
    "age":27,
    "tags":["developer", "tech geek"],
    "details":{
        "job":"full-stack developer",
        "organisation":"nic"
    },
    "created_at":datetime.datetime.utcnow()
}

# inserting one data using insert_one() function
result = test_collec.insert_one(sample_data)

#checking the inserted data using refrence_id
document_id = result.inserted_id
print("Inserted _id document:",document_id)
"""

# inserting multiple data using insert_many method
"""
sample_data_1 = {
    "name":"arun",
    "age":27,
    "tags":["pythonista", "cyborg"],
    "details":{
        "job":"AI/ML",
        "organisation":"xAI"
    },
    "created_at":datetime.datetime.utcnow()
}

sample_data_2 = {
    "name":"arunisto",
    "age":27,
    "tags":["backend", "fast api"],
    "details":{
        "job":"IOT Engineer",
        "organisation":"tesla"
    },
    "created_at":datetime.datetime.utcnow()
}

#using insert_many() function to insert multiple data
result = test_collec.insert_many([sample_data_1, sample_data_2])

document_ids = result.inserted_ids
print("No. Documents added:",len(document_ids))
print("_ids of inserted:\n",document_ids)
"""

#accessing a single data using find_one() function
"""
#query to access a data
# for use Object id in your program u need to import it from the bson object
id = {"_id":ObjectId('654e604707f115c93d316013')}
result = test_collec.find_one(id)
print("Retrieved data:\n",result)
#pprint using to print in a document form
pprint.pprint(result)
"""

#accessing all data/multiple data using find() function
"""
result = test_collec.find()
for document in result:
    pprint.pprint(document)
"""

# updating a single data using update_one() function
"""
document_to_update = {'_id': ObjectId('654e5e80ad5db1b63c82220c')}
field_to_update = {"$inc":{"age":1}}
result = test_collec.update_one(document_to_update, field_to_update)
print("Updated Count:",result.modified_count)
"""

#updating multiple document using update_many() function
"""
doc_filter = {"age":{"$eq":27}}
add_new_field = {"$inc":{"age":1}}
result = test_collec.update_many(doc_filter, add_new_field)
print("Document Matched:",result.matched_count)
print("Updated:",result.modified_count)
"""

#deleting documents using delete_one() and delete_many() method
"""
document_to_delete = {"name":"test1"}
#deleting using delete_one() method
result = test_collec.delete_one(document_to_delete)
print("No. of deleted documents:",result.deleted_count)
"""

#deleting multiple elements using delete_many() method
"""
doc_to_filter = {"age":{"$eq":28}}
result = test_collec.delete_many(doc_to_filter)
print("No.of Documents deleted:",result.deleted_count)
"""
client.close()



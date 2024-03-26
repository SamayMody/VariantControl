import pymongo
from bson import ObjectId

import os
from dotenv import load_dotenv
load_dotenv()

MongoURI = os.getenv('MongoURL')


client = pymongo.MongoClient(MongoURI)
db = client["Store"]
collection = db["Product"]

def create(data1 , data2):
    data = {"Product": data1.Product,
            "Variants": {"Size": data2.Size, "Color": data2.Color, "Material": data2.Material}}
    response = collection.insert_one(data)
    return str(response.inserted_id)

def get_all():
    response = collection.find({})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_product(condition):
    response = collection.find({"Product": condition})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_product_variant(size, color, material):
    response = collection.find({"Variants":{"Size": size, "Color": color, "Material": material}})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def update(id, data1, data2):
    response = collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "Product": data1.Product,
                "Variants.Size": data2.Size,
                "Variants.Color": data2.Color,
                "Variants.Material": data2.Material
            }
        }
    )

    return response.modified_count

def delete(id):
    response = collection.delete_one({"_id": ObjectId(id)})
    return response.deleted_count

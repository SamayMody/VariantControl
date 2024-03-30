import pymongo
from bson import ObjectId
from modal import Variants

import threading
lock = threading.Lock()

from dotenv import load_dotenv
import os

load_dotenv()
MongoURI = os.getenv('MongoURL')
client = pymongo.MongoClient(MongoURI)
db = client["Store"]
collection = db["Product"]

def create(data):
    with lock:
        response = collection.insert_one(data.dict())
        return response.inserted_id

def get_by_product(condition):
    response = collection.find({"Product": condition})
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    return data

def get_by_variant(size, color, material):
    response = collection.find({ "Variants": {"size": size, "color": color, "material": material}})
    data = []
    for i in response:
        data.append({"_id": str(i["_id"]), "Product": i["Product"]})
    return data

def update(product, id, variants):
    variant_data = {
        "size": variants.size,
        "color": variants.color,
        "material": variants.material
    }
    response = collection.update_one(
        {"Product": product, "Variants.id": id},
        {"$set": {
            "Variants.$.size": variant_data["size"],
            "Variants.$.color": variant_data["color"],
            "Variants.$.material": variant_data["material"]
        }}
    )
    return response.modified_count

def delete_variant(product, id):
    response = collection.update_one(
        {"Product": product},
        {"$pull": {
            "Variants": {"id": id}
        }}
    )
    return response.modified_count

def delete_product(product):
    response = collection.delete_one({"Product": product})
    return response.deleted_count


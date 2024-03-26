from fastapi import FastAPI
import db
from modal import Product, Variants

app = FastAPI()

@app.post("/upload/product")
def product_info(data1: Product, data2: Variants):
    id = db.create(data1, data2)
    return id

@app.get("/get/byproduct")
def product(product_name: str):
    data = db.get_product(product_name)
    return data

@app.get("/get/byvariant")
def variants(Size: str , Color: str , Material: str):
    data = db.get_product_variant(Size,Color,Material)
    return data

@app.put("/update/product_variant")
def update(id: str, data1: Product , data2: Variants):
    data = db.update(id, data1, data2)
    return {"updated": True, "data": data}

@app.delete("/delete/product")
def delete_product(id: str):
    data = db.delete(id)
    return {"deleted": True , "data": data}
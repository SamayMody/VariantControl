from fastapi import FastAPI
import db
from modal import Product, Variants, UpdateVariant


app = FastAPI()

@app.post("/upload/product")
def product_info(data: Product):
    id = db.create(data)
    return {"message": "Product uploaded successfully", "id": str(id)}

@app.get("/get/product")
def getting_by_product(product_name: str):
    data = db.get_by_product(product_name)
    if data:
        return data
    else:
        return {"message": "No such Product is available for the moment"}

@app.get("/get/variants")
def getting_by_variants(size: str, color: str, material: str):
    data = db.get_by_variant(size, color, material)
    if data:
        return data
    else:
        return {"message": "No such variant is available for the moment"}


@app.put("/update/product")
def updating_product(product: str, id: int, variants: UpdateVariant):
    data = db.update(product, id , variants)
    return data

@app.delete("/delete/product/variant")
def deleting_product_variant(product: str, id: int):
    data = db.delete_variant(product, id)
    return data

@app.delete("/delete/product/{product}")
def deleting_product(product: str):
    data = db.delete_product(product)
    if data == 1:
        return {"deleted": True, "message": f"Product '{product}' deleted successfully"}
    else:
        return {"deleted": False, "message": f"Product '{product}' not found"}

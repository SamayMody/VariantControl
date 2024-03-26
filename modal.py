from pydantic import BaseModel

class Product(BaseModel):
    Product: str

class Variants(BaseModel):
    Size: str
    Color: str
    Material: str

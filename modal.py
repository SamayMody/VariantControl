from pydantic import BaseModel
from typing import List

class Variants(BaseModel):
    id : int
    size: str
    color: str
    material: str

class Product(BaseModel):
    Product: str
    Variants: List[Variants]
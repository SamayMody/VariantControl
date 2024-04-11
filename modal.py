from pydantic import BaseModel
from typing import List , Optional

class Variants(BaseModel):
    id : Optional[int]
    size: str
    color: str
    material: str

class Product(BaseModel):
    Product: str
    Variants: List[Variants]

class UpdateVariant(BaseModel):
    size: str
    color: str
    material: str
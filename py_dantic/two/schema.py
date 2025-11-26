from pydantic import BaseModel

class Item(BaseModel):
    name: str
    qty: int
    price: float

class Object(BaseModel):
    orderId: int
    customer: str
    items: list[Item]

class FinalStructure(BaseModel):
    orders: list[Object]

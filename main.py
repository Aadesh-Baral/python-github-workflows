from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


api = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@api.get("/")
def system():
    return {"Hello": "World"}

@api.get("/items/{item_id}")
def items(item_id:int, q: Union[str, None]=None):
    return {"item_id": item_id, "q": q}


@api.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

api = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@api.get("/")
def system():
    return {"Hello": "World"}


@api.get("/items/{item_id}")
def items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@api.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@api.post("/release")
def add_release_version():
    latest_release = requests.get(
        "https://api.github.com/repos/Aadesh-Baral/python-github-workflows/releases/latest",
        headers={'Authorization':os.env.get("GITHUB_ACCESS_TOKEN")}
        )
    release_file = open("release.txt", "w")
    release_file.write(latest_release.json()['name'])
    return {"release": latest_release.json()['name']}

@api.get("/release")
def get_release_version():
    release_file = open("release.txt", "r")
    return {"release": release_file.read()}

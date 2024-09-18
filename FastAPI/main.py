from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API con FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item creado", "item": item}

@appping.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item actualizado", "item_id": item_id, "item": item}
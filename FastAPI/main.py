from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Lista para almacenar los items creados
items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de ejemplo de FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if item_id < len(items):
        return {"item_id": item_id, "item": items[item_id], "query": q}
    return {"error": "Item no encontrado"}

@app.post("/items/create")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item creado", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id < len(items):
        items[item_id] = item 
        return {"message": "Item actualizado", "item_id": item_id, "item": item}
    return {"error": "Item no encontrado"}

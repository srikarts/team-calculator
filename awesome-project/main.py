from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel



app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def sample_func():
    return {"message", "Hello FastAPI!"}

@app.get("/users/{user_id}")
def show_user(user_id: int):
    return {"userId": user_id, "User Name": f"User{user_id}"}

@app.get('/products/')
def show_prod(skip: int=10,limit: int=50):
    return {"skip": skip, 'limit': limit, 'products' : ['prod1','prod2','prod3']}


@app.post("/items/")
def create_item(item: Item):
    return {"item": item, "tax_calculated": item.price * 0.1}














# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
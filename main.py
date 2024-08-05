from typing import Union
from mangum import Mangum
from fastapi import FastAPI, Request
from decorators.rate_limiter import custom_limiter
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
@custom_limiter()
def read_item(request:Request):
    return {"item_id": item_id, "q": q}


handler=Mangum(app)
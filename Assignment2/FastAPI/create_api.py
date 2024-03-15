# import dotenv
# import os

# dotenv = dotenv.load_dotenv()

# api_one = os.getenv()
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
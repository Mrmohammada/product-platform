import os
from fastapi import FastAPI
from backend.api_client import call_api
from backend.formatter import toman
from backend.logger import log

app = FastAPI()
API_KEY = os.getenv("API_KEY")

@app.get("/products")
def products():
    data = call_api(API_KEY,"get_all_product_details")
    log("Products fetched")
    return data

from fastapi import FastAPI
from app.routers import massupload
import logging

logging.basicConfig(
    filename="app/logs/app.log",  
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

app.include_router(massupload.router, prefix="/v2/carbon_data/sheet_wise_mass_upload", tags=["Massupload"])
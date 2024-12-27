from pymongo import MongoClient
from bson import ObjectId
MONGO_DETAILS = "mongodb://localhost:27017" 

client = MongoClient(MONGO_DETAILS)
database = client['notch-stage-17-06']  
v2_carbon_data = database.get_collection("v2_carbon_data")


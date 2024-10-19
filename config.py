from pymongo import MongoClient

MONGO_URI = "mongodb://root:root@mongo:27017/spotfyql?authSource=admin"

def get_db():
    client = MongoClient(MONGO_URI)
    return client.spotfyql
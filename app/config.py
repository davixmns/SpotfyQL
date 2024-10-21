from pymongo import MongoClient
import os

mongo_uri = os.getenv("MONGO_URI")

def get_db():
    client = MongoClient(mongo_uri)
    return client.spotfyql

def test_connection():
    try:
        db = get_db()
        db.list_collection_names()
        print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexão: {e}")
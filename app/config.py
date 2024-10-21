from pymongo import MongoClient

MONGO_URI = "mongodb://root:root@localhost:27017/spotfyql?authSource=admin"

def get_db():
    client = MongoClient(MONGO_URI)
    return client.spotfyql

def test_connection():
    try:
        db = get_db()
        db.list_collection_names()
        print("Conexão bem-sucedida!")
    except Exception as e:
        print(f"Erro na conexão: {e}")
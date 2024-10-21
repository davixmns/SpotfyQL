from bson import ObjectId
from pymongo.synchronous.collection import Collection

from app.config import get_db


class BaseRepository:
    def __init__(self, entity_class, collection_name):
        self.db = get_db()
        self.entity_class = entity_class
        self.collection: Collection = self.db[collection_name]

    def get_all(self):
        docs = self.collection.find()
        return [self.entity_class(**doc) for doc in docs]

    def find_one(self, criteria):
        doc = self.collection.find_one(criteria)
        if not doc:
            return None
        return self.entity_class(**doc)

    def create(self, entity):
        result = self.collection.insert_one(entity.__dict__)
        entity.id = str(result.inserted_id)
        return self.entity_class(**entity)

    def update(self, entity_id, update_data):
        self.collection.update_one(
            {"_id": ObjectId(entity_id)},
            {"$set": update_data}
        )

    def delete(self, entity_id):
        self.collection.delete_one({"_id": ObjectId(entity_id)})

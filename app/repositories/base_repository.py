from bson import ObjectId

from pymongo.synchronous.database import Database

class BaseRepository:
    def __init__(self, db: Database, entity_class, collection_name):
        self.db = db
        self.entity_class = entity_class
        self.collection = db[collection_name]

    def get_all(self):
        docs = self.collection.find()
        return [self.entity_class(**doc) for doc in docs]

    def get_by_criteria(self, criteria):
        docs = self.collection.find(criteria)
        return [self.entity_class(**doc) for doc in docs]

    def create(self, entity):
        result = self.collection.insert_one(entity.__dict__)
        entity.id = str(result.inserted_id)
        return entity

    def update(self, entity_id, update_data):
        self.collection.update_one(
            {"_id": ObjectId(entity_id)},
            {"$set": update_data}
        )

    def delete(self, entity_id):
        self.collection.delete_one({"_id": ObjectId(entity_id)})

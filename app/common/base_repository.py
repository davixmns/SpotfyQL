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
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        doc = self.collection.find_one(criteria)
        return self.entity_class(**doc) if doc else None

    def find(self, criteria):
        docs = self.collection.find(criteria)
        return [self.entity_class(**doc) for doc in docs]

    def create(self, entity):
        result = self.collection.insert_one(entity.to_bson())
        entity.id = str(result.inserted_id)
        entity.to_bson()

        return entity

    # In your BaseRepository
    def update(self, entity_id, update_data):
        # Remove '_id' from update_data if it exists
        update_data.pop("_id", None)
        updated_entity = self.collection.find_one_and_update(
            {"_id": ObjectId(entity_id)},
            {"$set": update_data},
            return_document=True
        )
        return self.entity_class(**updated_entity) if updated_entity else None

    def delete(self, entity_id):
        self.collection.delete_one({"_id": ObjectId(entity_id)})
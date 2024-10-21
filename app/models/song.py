from pydantic import BaseModel, Field
from typing import List, Optional

from app.models.objectid import PydanticObjectId

class Song(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    title: str
    artist: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls.model_validate(data)

    def to_bson(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        data.pop("_id", None)
        return data
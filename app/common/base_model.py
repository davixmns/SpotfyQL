from typing import Optional
from pydantic import BaseModel, Field
from app.common.objectid import PydanticObjectId

class MyBaseModel(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def to_bson(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        data.pop("_id", None)
        return data

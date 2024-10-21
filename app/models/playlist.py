from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field
from app.models.objectid import PydanticObjectId


class Playlist(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    name: str
    description: str
    songs: List[PydanticObjectId] = []
    date_created: Optional[datetime] = None

    def to_bson(self):
        data = self.dict(by_alias=True, exclude_none=True)
        if data["_id"] is None:
            data.pop("_id")
        return data
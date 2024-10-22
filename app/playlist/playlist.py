from typing import List

from app.common.base_model import MyBaseModel
from app.common.objectid import PydanticObjectId

class Playlist(MyBaseModel):
    name: str
    description: str
    songs: List[PydanticObjectId] = []
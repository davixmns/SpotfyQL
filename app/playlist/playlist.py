from datetime import datetime
from typing import Optional, List

from app.common.base_model import MyBaseModel
from app.common.objectid import PydanticObjectId


class Playlist(MyBaseModel):
    name: str
    description: str
    songs: List[PydanticObjectId] = []
    date_created: Optional[datetime] = None
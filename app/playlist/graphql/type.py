from typing import List

import strawberry
from app.song.graphql.type import SongType

@strawberry.type
class PlaylistType:
    id: str
    name: str
    description: str
    songs: List[SongType]
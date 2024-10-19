from typing import List

import strawberry
from app.graphql.song.type import SongType

@strawberry.type
class PlaylistType:
    id: str
    name: str
    description: str
    songs: List[SongType]
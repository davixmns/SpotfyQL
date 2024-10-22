import strawberry
from typing import List 
from app.song.graphql.type import SongType
from app.song.song_service import SongService

@strawberry.type
class SongQueries:

    @strawberry.field()
    def songs(self) -> List[SongType]:
        return SongService().get_all_songs()

    @strawberry.field()
    def song(self, song_id: str) -> SongType:
        return SongService().get_song_by_id(song_id)

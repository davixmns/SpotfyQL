import strawberry
from typing import List  # Corrigir para usar List do typing
from app.graphql.song.type import SongType
from app.services.song_service import SongService

@strawberry.type
class SongQueries:
    def __init__(self, info):
        self.service = SongService(info.context['db'])

    @strawberry.field()
    def songs(self) -> List[SongType]:  # Corrigido: List ao invés de []
        return self.service.get_all_songs()

    @strawberry.field()
    def song(self, song_id: str) -> SongType:
        return self.service.get_song_by_id(song_id)

import strawberry
from typing import List  # Corrigir para usar List do typing
from app.graphql.playlist.type import PlaylistType
from app.services.playlist_service import PlaylistService

@strawberry.type
class PlaylistQueries:
    def __init__(self, info):
        self.service = PlaylistService(info.context['db'])

    @strawberry.field()
    def playlists(self) -> List[PlaylistType]:  # Corrigido: List ao invés de []
        playlists = self.service.get_all_playlists()
        return [PlaylistType(**playlist.__dict__) for playlist in playlists]

    @strawberry.field()
    def playlist(self, playlist_id: str) -> PlaylistType:
        return self.service.get_playlist_by_id(playlist_id)

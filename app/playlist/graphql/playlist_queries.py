import strawberry
from typing import List
from app.playlist.graphql.playlist_type import PlaylistType
from app.playlist.playlist_service import PlaylistService


@strawberry.type
class PlaylistQueries:

    @strawberry.field()
    def playlists(self) -> List[PlaylistType]:
        playlists = PlaylistService().get_all_playlists()
        return [PlaylistType(**playlist.__dict__) for playlist in playlists]

    @strawberry.field()
    def playlist(self, playlist_id: str) -> PlaylistType:
        return PlaylistService().get_playlist_by_id(playlist_id)

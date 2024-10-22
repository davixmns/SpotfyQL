import strawberry
from typing import List
from app.playlist.graphql.playlist_type import PlaylistType
from app.playlist.playlist_service import PlaylistService


@strawberry.type
class PlaylistQueries:

    @strawberry.field()
    def playlists(self) -> List[PlaylistType]:
        playlists = PlaylistService().get_all_playlists()
        for playlist in playlists:
            yield PlaylistType(
                id=str(playlist.id),
                name=playlist.name,
                description=playlist.description,
                songs_ids=[str(song_id) for song_id in playlist.songs]
            )

    @strawberry.field()
    def playlist(self, playlist_id: str) -> PlaylistType:
        return PlaylistService().get_playlist_by_id(playlist_id)

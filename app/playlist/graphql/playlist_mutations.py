import strawberry

from app.playlist.playlist import Playlist
from app.playlist.graphql.playlist_type import PlaylistType
from app.playlist.playlist_service import PlaylistService


@strawberry.type
class PlaylistMutations:

    @strawberry.mutation()
    def create_playlist(self, name: str, description: str) -> PlaylistType:
        created_playlist = PlaylistService().create_playlist(Playlist(name=name, description=description))
        return PlaylistType(**created_playlist.__dict__)

    @strawberry.mutation()
    def add_song_to_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = PlaylistService().add_song_to_playlist(playlist_id, song_id)
        return PlaylistType(**updated_playlist.__dict__)

    @strawberry.mutation()
    def remove_song_from_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = PlaylistService().remove_song_from_playlist(playlist_id, song_id)
        return PlaylistType(**updated_playlist.__dict__)
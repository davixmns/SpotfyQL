import strawberry

from app.playlist.playlist import Playlist
from app.playlist.graphql.type import PlaylistType
from app.playlist.playlist_service import PlaylistService

@strawberry.type
class PlaylistMutations:
    def __init__(self, info):
        self.service = PlaylistService()

    @strawberry.mutation()
    def create_playlist(self, name: str, description: str) -> PlaylistType:
        new_playlist = Playlist(name, description)
        created_playlist = self.service.create_playlist(new_playlist)
        return PlaylistType(**created_playlist.__dict__)

    @strawberry.mutation()
    def add_song_to_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = self.service.add_song_to_playlist(playlist_id, song_id)
        return PlaylistType(**updated_playlist.__dict__)

    @strawberry.mutation()
    def remove_song_from_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = self.service.remove_song_from_playlist(playlist_id, song_id)
        return PlaylistType(**updated_playlist.__dict__)
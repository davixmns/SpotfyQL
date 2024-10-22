import strawberry

from app.playlist.playlist import Playlist
from app.playlist.graphql.playlist_type import PlaylistType
from app.playlist.playlist_service import PlaylistService

@strawberry.type
class PlaylistMutations:

    @strawberry.mutation()
    def create_playlist(self, name: str, description: str) -> PlaylistType:
        created_playlist = PlaylistService().create_playlist(Playlist(name=name, description=description))
        return PlaylistType(
            id=str(created_playlist.id),
            name=created_playlist.name,
            description=created_playlist.description,
            songs_ids=[str(song_id) for song_id in created_playlist.songs]
        )

    @strawberry.mutation()
    def add_song_to_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = PlaylistService().add_song_to_playlist(playlist_id, song_id)
        return PlaylistType(
            id=str(updated_playlist.id),
            name=updated_playlist.name,
            description=updated_playlist.description,
            songs_ids=[str(song_id) for song_id in updated_playlist.songs]
        )

    @strawberry.mutation()
    def remove_song_from_playlist(self, playlist_id: str, song_id: str) -> PlaylistType:
        updated_playlist = PlaylistService().remove_song_from_playlist(playlist_id, song_id)
        return PlaylistType(
            id=str(updated_playlist.id),
            name=updated_playlist.name,
            description=updated_playlist.description,
            songs_ids=[str(song_id) for song_id in updated_playlist.songs]
        )
from app.models.playlist import Playlist
from app.repositories.base_repository import BaseRepository

class PlaylistRepository(BaseRepository):
    def __init__(self):
        super().__init__(Playlist, "playlists")
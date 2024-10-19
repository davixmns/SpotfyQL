from app.entities.playlist import Playlist
from app.repositories.base_repository import BaseRepository

class PlaylistRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Playlist, "playlists")
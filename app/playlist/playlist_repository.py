from app.playlist.playlist import Playlist
from app.common.base_repository import BaseRepository

class PlaylistRepository(BaseRepository):
    def __init__(self):
        super().__init__(Playlist, "playlists")
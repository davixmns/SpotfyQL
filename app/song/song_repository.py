from app.common.base_repository import BaseRepository
from app.song.song import Song

class SongRepository(BaseRepository):
    def __init__(self):
        super().__init__(Song, "songs")

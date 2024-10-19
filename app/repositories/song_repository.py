from app.repositories.base_repository import BaseRepository
from app.entities.song import Song

class SongRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, Song, "songs")
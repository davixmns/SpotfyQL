from pymongo.synchronous.database import Database

from app.entities.song import Song
from app.repositories.song_repository import SongRepository

class SongService:
    def __init__(self, db: Database):
        self.repository = SongRepository(db)

    def get_all_songs(self) -> [Song]:
        return self.repository.get_all()

    def create_song(self, song) -> Song:
        song_exists = self.repository.get_by_criteria({"title": song.title})

        if song_exists:
            raise Exception("Song already exists")

        return self.repository.create(song)

    def get_song_by_id(self, song_id) -> Song or None:
        return self.repository.get_by_criteria({"_id": song_id})

    def update_song(self, song_id, update_data) -> Song:
        song_exists = self.repository.get_by_criteria({"_id": song_id})

        if not song_exists:
            raise Exception("Song does not exist")

        return self.repository.update(song_id, update_data)
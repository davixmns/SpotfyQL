from bson import ObjectId

from app.common.objectid import PydanticObjectId
from app.song.song_repository import SongRepository
from app.song.song import Song

class SongService:
    def __init__(self):
        self.repository = SongRepository()

    def get_all_songs(self) -> [Song]:
        songs = self.repository.get_all()
        return songs

    def find_many(self, song_ids) -> [Song]:
        return self.repository.find({"_id": {"$in": [ObjectId(song_id) for song_id in song_ids]}})

    def create_song(self, song) -> Song:
        song_exists = self.repository.find_one({"title": song.title})

        if song_exists:
            raise Exception("Song already exists")

        return self.repository.create(song)

    def get_song_by_id(self, song_id) -> Song or None:
        return self.repository.find_one({"_id": PydanticObjectId(song_id)})

    def update_song(self, song_id, update_data) -> Song:
        return self.repository.update(song_id, update_data)
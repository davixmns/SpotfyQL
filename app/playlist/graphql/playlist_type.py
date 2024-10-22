from typing import List
import strawberry
from strawberry import Private

from app.song.graphql.song_type import SongType
from app.song.song import Song
from app.song.song_repository import SongRepository
from bson import ObjectId

from app.song.song_service import SongService


@strawberry.type
class PlaylistType:
    id: str
    name: str
    description: str

    def __init__(self, id: str, name: str, description: str, songs_ids: List[str]):
        self.id = id
        self.name = name
        self.description = description
        self.songs_ids = songs_ids

    @strawberry.field()
    def songs(self, info) -> List[SongType]:
        song_service = SongService()

        songs = song_service.find_many(self.songs_ids)

        song_types = [SongType(id=str(song.id), title=song.title, artist=song.artist) for song in songs]

        return song_types


        # song_repository = SongRepository()
        #
        # song_ids = [ObjectId(song_id) for song_id in self.songs_ids]
        #
        # songs = song_repository.find({"_id": {"$in": song_ids}})
        #
        # song_types = [SongType(id=str(song.id), title=song.title, artist=song.artist) for song in songs]
        #
        # return song_types
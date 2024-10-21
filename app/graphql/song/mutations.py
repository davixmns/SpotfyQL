import strawberry

from app.entities.song import Song
from app.graphql.song.type import SongType
from app.services.song_service import SongService

@strawberry.type
class SongMutations:

    @strawberry.mutation()
    def create_song(self, title: str, artist: str) -> SongType:
        new_song = SongService().create_song(Song(title, artist))
        return SongType(**new_song)

    @strawberry.mutation()
    def update_song(self, song_id: str, title: str, artist: str) -> SongType:
        updated_song = SongService().update_song(song_id, Song(title, artist))
        return SongType(**updated_song.__dict__)
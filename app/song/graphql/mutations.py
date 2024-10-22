import strawberry

from app.song.song import Song
from app.song.graphql.type import SongType
from app.song.song_service import SongService

@strawberry.type
class SongMutations:
    @strawberry.mutation()
    def create_song(self, title: str, artist: str) -> SongType:
        new_song = SongService().create_song(Song(title=title, artist=artist))
        return SongType(**new_song.__dict__)

    @strawberry.mutation()
    def update_song(self, song_id: str, title: str, artist: str) -> SongType:
        updated_song = SongService().update_song(song_id, {"title": title, "artist": artist})
        return SongType(**updated_song.__dict__)
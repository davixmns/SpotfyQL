import strawberry

@strawberry.type
class SongType:
    id: str
    title: str
    artist: str

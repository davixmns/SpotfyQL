import strawberry
from app.playlist.graphql.playlist_queries import PlaylistQueries
from app.playlist.graphql.playlist_mutations import PlaylistMutations
from app.song.graphql.song_queries import SongQueries
from app.song.graphql.song_mutations import SongMutations

@strawberry.type
class Query(PlaylistQueries, SongQueries):
    pass

@strawberry.type
class Mutation(PlaylistMutations, SongMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
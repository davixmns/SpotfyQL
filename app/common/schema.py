import strawberry
from app.playlist.graphql.queries import PlaylistQueries
from app.playlist.graphql.mutations import PlaylistMutations
from app.song.graphql.queries import SongQueries
from app.song.graphql.mutations import SongMutations

@strawberry.type
class Query(PlaylistQueries, SongQueries):
    pass

@strawberry.type
class Mutation(PlaylistMutations, SongMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
import strawberry
from app.graphql.playlist.queries import PlaylistQueries
from app.graphql.playlist.mutations import PlaylistMutations
from app.graphql.song.queries import SongQueries
from app.graphql.song.mutations import SongMutations

@strawberry.type
class Query(PlaylistQueries, SongQueries):
    pass

@strawberry.type
class Mutation(PlaylistMutations, SongMutations):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
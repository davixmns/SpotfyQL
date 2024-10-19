
class Playlist:
    def __init__(self, name, description, songs=None, _id=None):
        self.id = str(_id) or None
        self.name = name
        self.description = description
        self.songs = songs or []
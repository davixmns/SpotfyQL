from app.entities.base_entity import BaseEntity


class Playlist(BaseEntity):
    def __init__(self, name, description, songs=None, _id=None):
        self.id = str(_id) if _id else None
        self.name = name
        self.description = description
        self.songs = songs or []
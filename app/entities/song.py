from app.entities.base_entity import BaseEntity


class Song(BaseEntity):
    def __init__(self, title, artist, _id=None):
        self.id = str(_id) if _id else None
        self.title = title
        self.artist = artist
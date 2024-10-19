
class Song:
    def __init__(self, title, artist, _id=None):
        self.id = str(_id) or None
        self.title = title
        self.artist = artist

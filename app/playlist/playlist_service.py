from app.playlist.playlist import Playlist
from app.playlist.playlist_repository import PlaylistRepository
from app.song.song import Song
from app.song.song_repository import SongRepository

class PlaylistService:
    def __init__(self):
        self.playlist_repository = PlaylistRepository()
        self.song_repository = SongRepository()

    def get_all_playlists(self) -> [Playlist]:
        return self.playlist_repository.get_all()

    def create_playlist(self, playlist) -> Playlist:
        repository_exists = self.playlist_repository.find_one({"name": playlist.name})

        if repository_exists:
            raise Exception("Playlist already exists")

        return self.playlist_repository.create(playlist)

    def get_playlist_by_id(self, playlist_id) -> Playlist or None:
        return self.playlist_repository.find_one({"_id": playlist_id})

    # In your PlaylistService
    def add_song_to_playlist(self, playlist_id, song_id) -> Playlist:
        playlist: Playlist = self.playlist_repository.find_one({"_id": playlist_id})
        song: Song = self.song_repository.find_one({"_id": song_id})

        if not playlist or not song:
            raise Exception("Playlist or Song not found")

        playlist.songs.append(song.id)

        updated_playlist = self.playlist_repository.update(playlist_id, {"songs": playlist.songs})

        return updated_playlist

    def remove_song_from_playlist(self, playlist_id, song_id):
        playlist = self.playlist_repository.find_one({"_id": playlist_id})
        song = self.song_repository.find_one({"_id": song_id})

        if not playlist or not song:
            raise Exception("Playlist or Song not found")

        if not song in playlist.songs:
            raise Exception("Song not in playlist")

        playlist.songs.remove(song)

        return self.playlist_repository.update(playlist_id, playlist)

    def delete_playlist(self, playlist_id):
        playlist_exists = self.playlist_repository.find_one({"_id": playlist_id})

        if not playlist_exists:
            raise Exception("Playlist not found")

        return self.playlist_repository.delete(playlist_id)
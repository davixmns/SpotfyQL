from typing import List

from pymongo.synchronous.database import Database

from app.entities.playlist import Playlist
from app.repositories.playlist_repository import PlaylistRepository
from app.repositories.song_repository import SongRepository


class PlaylistService:
    def __init__(self, db: Database):
        self.playlist_repository = PlaylistRepository(db)
        self.song_repository = SongRepository(db)

    def get_all_playlists(self) -> [Playlist]:
        return self.playlist_repository.get_all()

    def create_playlist(self, playlist) -> Playlist:
        repository_exists = self.playlist_repository.get_by_criteria({"name": playlist.name})

        if repository_exists:
            raise Exception("Playlist already exists")

        return self.playlist_repository.create(playlist)

    def get_playlist_by_id(self, playlist_id) -> Playlist or None:
        return self.playlist_repository.get_by_criteria({"_id": playlist_id})

    def update_playlist(self, playlist_id, update_data) -> Playlist:
        playlist_exists = self.playlist_repository.get_by_criteria({"_id": playlist_id})

        if not playlist_exists:
            raise Exception("Playlist not found")

        return self.playlist_repository.update(playlist_id, update_data)

    def add_song_to_playlist(self, playlist_id, song_id) -> Playlist:
        playlist = self.playlist_repository.get_by_criteria({"_id": playlist_id})
        song = self.song_repository.get_by_criteria({"_id": song_id})

        if not playlist or not song:
            raise Exception("Playlist or Song not found")

        playlist.songs.append(song)

        return self.playlist_repository.update(playlist_id, playlist)

    def remove_song_from_playlist(self, playlist_id, song_id):
        playlist = self.playlist_repository.get_by_criteria({"_id": playlist_id})
        song = self.song_repository.get_by_criteria({"_id": song_id})

        if not playlist or not song:
            raise Exception("Playlist or Song not found")

        if not song in playlist.songs:
            raise Exception("Song not in playlist")

        playlist.songs.remove(song)

        return self.playlist_repository.update(playlist_id, playlist)

    def delete_playlist(self, playlist_id):
        playlist_exists = self.playlist_repository.get_by_criteria({"_id": playlist_id})

        if not playlist_exists:
            raise Exception("Playlist not found")

        return self.playlist_repository.delete(playlist_id)
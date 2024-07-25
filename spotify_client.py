import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE

class SpotifyClient:
    def __init__(self):
        self.auth_manager = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE)
        self.sp = None

    def get_auth_url(self):
        return self.auth_manager.get_authorize_url()

    def get_token(self, code):
        token_info = self.auth_manager.get_access_token(code)
        self.sp = spotipy.Spotify(auth=token_info['access_token'])
        return token_info

    def get_user_playlists(self):
        playlists = self.sp.current_user_playlists()
        return playlists['items']

    def get_playlist_tracks(self, playlist_id):
        results = self.sp.playlist_tracks(playlist_id)
        tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            tracks.extend(results['items'])
        return tracks

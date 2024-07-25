from spotify_client import SpotifyClient
from openai_client import OpenAIClient

class Recommender:
    def __init__(self):
        self.spotify_client = SpotifyClient()
        self.openai_client  = OpenAIClient()

    def get_recommendations_for_user(self):
        playlists = self.spotify_client.get_user_playlists()
        first_playlist_id = playlists['items'][0]['id']
        tracks = self.spotify_client.get_playlist_tracks(first_playlist_id)
        recommendations = self.openai_client.generate_recommendations(tracks)
        return recommendations
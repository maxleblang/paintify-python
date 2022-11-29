import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv



class SpotifyUser:
    """Initialize a SpotifyUser object"""
    def __init__(self) -> None:
        pass
    
    """Function to authenticate a user with the Spotify API using OAuth 2.0
    :param: .env file containing client environment variables
    :returns: an authenticated client object
    """
    def authenticate(self):
        #load in environment vairables for API authentication
        load_dotenv()
        # Shows a user's playlists
        scope = 'playlist-read-private'
        client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        return client
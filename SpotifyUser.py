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
        scope = 'playlist-read-private playlist-modify-private ugc-image-upload playlist-modify-public'
        client = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        print("Spotify authenticated")
        self.sp = client

    def get_playlists(self):
        #get all user playlists
        playlist_data = self.sp.current_user_playlists(limit=50)['items']
        #loop through every playlist
        playlists = {}
        for playlist in playlist_data:
            name = playlist['name']
            id = playlist['uri']
            playlists[name] = id

        return playlists
    
    def set_playlist_cover_img(self,playlist_id,base64_str):
        self.sp.playlist_upload_cover_image(playlist_id,base64_str)
        print('Set playlist cover image')
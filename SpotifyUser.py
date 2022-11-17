import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyUser:
    def __init__(self) -> None:
        pass

    def authenticate(self):
        # Shows a user's playlists
        scope = 'playlist-read-public'
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    def get_playlists(self):
        results = self.sp.current_user_playlists(limit=50)
        for i, item in enumerate(results['items']):
            print("%d %s" % (i, item['name']))
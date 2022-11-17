from SpotifyUser import SpotifyUser as su

user = su()
user.authenticate()
user.get_playlists()
from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg

user = su()
client = user.authenticate()
gen = dg(client)

playlists = gen.get_playlists()
print(playlists)
songs = gen.get_songs(playlists['Penthouse'])
print(gen.average_song_features(songs))
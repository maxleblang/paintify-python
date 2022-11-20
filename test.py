from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg

user = su()
client = user.authenticate()
gen = dg(client)

x,ids = gen.get_playlists()

print(gen.get_songs(ids[0]))
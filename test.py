from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg

user = su()
client = user.authenticate()
generator = dg(client)
print(generator.get_playlists())
from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg
from ImageGenerator import ImageGenerator as ig



#generate array of playlists
user = su()
user.authenticate()
playlists = user.get_playlists()
p_id = playlists['2140 test']
print(p_id)

img_gen = ig()
img = img_gen.generate_image("Dog eating a tree")
b64_str = img.b64

user.set_playlist_cover_img(p_id,b64_str)


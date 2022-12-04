from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg
from ImageGenerator import ImageGenerator as ig

user = su()
sp = user.authenticate()
playlists = user.get_playlists()
name = 'Overtures and symphonies'
p_id = playlists[name]
des_gen = dg(sp)
description = des_gen.generate_description(p_id,name)
print(description)
img_gen = ig()
img = img_gen.generate_image(description)
b64_str = img.b64
user.set_playlist_cover_img(p_id,b64_str)
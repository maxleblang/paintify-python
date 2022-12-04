from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg
from ImageGenerator import ImageGenerator as ig

#generate array of playlists
user = su()
client_auth = user.authenticate()
playlists = user.get_playlists()
#create generators
desc_gen = dg(client_auth)
img_gen = ig()
#loop through playlists
for playlist,playlist_id in playlists:
    #generate description
    description = desc_gen.generate_description(playlist_id)
    #generate image
    img = img_gen.generate_image(description)
    #set playlist cover
    user.set_playlist_cover_img(img.base64_str,playlist_id)
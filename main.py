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
for playlist_name,playlist_id in playlists.items():
    if playlist_name == 'Songs I would play if I were in a band': #if statement just for controlled testing
        #generate description
        description = desc_gen.generate_description(playlist_id,playlist_name)
        print('Generating image with description:',description)
        #generate image
        img = img_gen.generate_image(description)
        #set playlist cover
        user.set_playlist_cover_img(playlist_id,img.b64)
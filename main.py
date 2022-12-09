from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg
from ImageGenerator import ImageGenerator as ig

def main1(playlist):
    user = su()
    client_auth = user.authenticate()
    playlists = playlist
    #create generators
    desc_gen = dg(client_auth)
    img_gen = ig()
    #loop through playlists
    print(playlists)
    for playlist_name,playlist_id in playlists.items():
        #if playlist_name == 'Skiing 2018-2019': #if statement just for controlled testing
            #generate description
        description = desc_gen.generate_description(playlist_id,playlist_name)
        print('Generating image with description:',description)
        #generate image
        img = img_gen.generate_image(description)
        #set playlist cover
        user.set_playlist_cover_img(playlist_id,img.b64)
    return True
from SpotifyUser import SpotifyUser as su
from DescriptionGenerator import DescriptionGenerator as dg
from ImageGenerator import ImageGenerator as ig

# img_gen = ig()
# url = img_gen.generate_image("A penguin smoking a blunt on saturns rings")
# print(url)
url = 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-9CFQXlwoo66gktBpAXqcNfY6/user-BfJb1osH29kwNkHjbMAuffqc/img-MWWgHyEE14mfxonR52iJd6G3.png?st=2022-12-01T23%3A18%3A27Z&se=2022-12-02T01%3A18%3A27Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-01T18%3A46%3A42Z&ske=2022-12-02T18%3A46%3A42Z&sks=b&skv=2021-08-06&sig=kO4A1YTAgng504H/furWU%2B6ZhUmP2n9LBs8sE7H0PrE%3D'




'''
user = su()
client = user.authenticate()
gen = dg(client)
playlists = gen.get_playlists()
print(playlists)
songs = gen.get_songs(playlists['Penthouse'])
print(gen.average_song_features(songs))
'''
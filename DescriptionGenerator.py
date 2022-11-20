import json
class DescriptionGenerator:
    """Initialize a DesciptionGenerator object"""
    def __init__(self,client) -> None:
        self.sp = client
        pass
    
    def get_playlists(self):
        #get all user playlists
        playlists = self.sp.current_user_playlists(limit=50)['items']
        #loop through every playlist
        playlist_names = []
        playlist_ids = []
        for playlist in playlists:
            playlist_names.append(playlist['name'])
            playlist_ids.append(playlist['uri'])

        return playlist_names,playlist_ids
    

    def get_songs(self,playlist_id):
        #get the JSON data for all songs in the playlist
        songs = self.sp.playlist_items(playlist_id)['items']

        #compile all the song names
        song_names = []
        song_ids = []
        for song in songs:
            track = song['track']
            name = track['name']
            id = track['uri']
            song_names.append(name)
            song_ids.append(id)

        return song_names,song_ids
class DescriptionGenerator:
    """Initialize a DesciptionGenerator object"""
    def __init__(self,client) -> None:
        self.sp = client
        pass
    
    def get_playlists(self):
        #get all user playlists
        playlists = self.sp.current_user_playlists(limit=50)['items']
        #loop through every playlist
        p_data = {}
        for playlist in playlists:
            name = playlist['name']
            id = playlist['uri']
            p_data[name] = id

        return p_data
    
    def get_songs(self,playlist_id):
        #get the JSON data for all songs in the playlist
        songs = self.sp.playlist_items(playlist_id)['items']
        #compile all the song names
        s_data = {}
        for song in songs:
            track = song['track']
            name = track['name']
            id = track['uri']
            s_data[name] = id

        return s_data
    
    def average_song_features(self,songs):
        #compile list of song ids and get audio features for all songs in playlist
        ids = [songs[key] for key in songs]
        song_data = self.sp.audio_features(ids)
        #avergae all values
        avg = {'danceability': 0,
               'energy': 0,
               'key': 0,
               'loudness': 0,
               'mode': 0,
               'speechiness': 0,
               'acousticness': 0,
               'instrumentalness': 0,
               'liveness': 0,
               'valence': 0,
               'tempo': 0
        }
        #add all values
        for data in song_data:
            for key, val in avg.items():
                #add to average dicitonary
                avg[key] += data[key]
        #divice by n
        for key,val in avg.items():
            avg[key] = val/len(song_data)
        
        return avg
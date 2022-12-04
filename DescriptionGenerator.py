import random
class DescriptionGenerator:
    #creating static variables for the description generation
    IMAGE_STYLE = ['Vincent van gogh style painting','trippy painting','lomography','neon lights','digital art']
    DANCE_ADJ = ['relaxed','trippy','groovy','hype']
    ENERGY_ADJ = ['peaceful','chill','happy','Exciting']


    """Initialize a DesciptionGenerator object"""
    def __init__(self,client) -> None:
        self.sp = client
        pass
    
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
        #average all values
        #add all values
        for data in song_data:
            for key, val in avg.items():
                #add to average dicitonary
                avg[key] += data[key]
        #divide by n
        for key,val in avg.items():
            avg[key] = val/len(song_data)
        
        return avg
    
    def choose_adj(self,lower_bound,upper_bound,score,adj_list):
        score_range = upper_bound-lower_bound
        interval = score_range/len(adj_list)
        for i in range(0,len(adj_list)):
            lower = lower_bound + (interval*i)
            upper = lower_bound + (interval*(i+1))
            if score >= lower and score <= upper:
                return adj_list[i]



    
    def generate_description(self,playlist_id,song_name):
        songs = self.get_songs(playlist_id)
        features = self.average_song_features(songs)
        style = random.choice(self.IMAGE_STYLE)
        dance_adj = self.choose_adj(0.1,0.8,features['danceability'],self.DANCE_ADJ)
        energy_adj = self.choose_adj(0.1,0.9,features['energy'],self.ENERGY_ADJ)
        description = f'A {dance_adj}, {energy_adj} {style} of {song_name}'
        
        return description
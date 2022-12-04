import random
class DescriptionGenerator:
    #creating static characteristic variables
    IMAGE_STYLE = ['Vincent van gogh style painting','trippy painting','lomography','neon lights','digital art']
    DANCE_ADJ = ['relaxed','trippy','groovy','hype']
    ENERGY_ADJ = ['peaceful','chill','happy','Exciting']

    """Initialize a DesciptionGenerator object"""
    def __init__(self,client) -> None:
        self.sp = client
        pass
    
    """Function that gets all the songs in a playlist
    :param playlist_id: the spotify playlist id
    :returns: a dictionary with the key as the song name and the value as the spotify track id
    """
    def get_songs(self,playlist_id):
        #get the JSON data for all songs in the playlist
        songs = self.sp.playlist_items(playlist_id)['items']
        #compile all the song names
        s_data = {}
        for song in songs:
            track = song['track']
            name = track['name']
            track_id = track['uri']
            s_data[name] = track_id

        return s_data
    
    """Function that gets the features of all the songs in a playlist and averages them
    :param songs: dictionary of all the songs in a playlist with the key being the song name and the value being the spotify track id
    :returns: dictionary of the average score of all the song features in the playlist
    """
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
    
    """Function that chooses an adjective from the list of adjectives based on the playlist's feature score
    :param lower_bound: lower bound of the score range
    :param upper_bound: upper bound of the score range
    :param score: the playlist's feature score
    :param adj_list: list of adjective strings
    :returns: the adjective that corresponds with the feature score
    """
    def choose_adj(self,lower_bound,upper_bound,score,adj_list):
        #Find interval ranges for the adjective list indexes
        score_range = upper_bound-lower_bound
        interval = score_range/len(adj_list)
        #find which interval the playlist's feature score falls in
        for i in range(0,len(adj_list)):
            lower = lower_bound + (interval*i)
            upper = lower_bound + (interval*(i+1))
            if score >= lower and score <= upper:
                return adj_list[i]
    
    """Function that generates an image description for a given playlist
    :param playlist_id: the spotify playlist id
    :param playlist_name: the name of the spotify playlist
    :returns: a unique image description for a given playlist based on a random style and it's average song features
    """
    def generate_description(self,playlist_id,playlist_name):
        #get all the songs from a playlist and find the average score for all song features
        songs = self.get_songs(playlist_id)
        features = self.average_song_features(songs)
        #choose a random style for variety
        style = random.choice(self.IMAGE_STYLE)
        #choose adjectives that correspond to the playlist's danceability and energy features
        dance_adj = self.choose_adj(0.1,0.8,features['danceability'],self.DANCE_ADJ)
        energy_adj = self.choose_adj(0.1,0.9,features['energy'],self.ENERGY_ADJ)
        #compile all parts of the description
        description = f'A {dance_adj}, {energy_adj} {style} of {playlist_name}'
        
        return description
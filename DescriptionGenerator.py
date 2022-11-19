class DescriptionGenerator:
    """Initialize a DesciptionGenerator object"""
    def __init__(self,client) -> None:
        self.sp = client
        pass
    
    def get_playlists(self):
        #get all user playlists
        playlists = self.sp.current_user_playlists(limit=50)['items']
        #loop through every playlist
        results = []
        for playlist in playlists:
            results.append(playlist['name'])
            #print("%d %s" % (i, item['name']))
        return results
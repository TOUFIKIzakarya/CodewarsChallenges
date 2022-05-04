L = list()
class Song:
    global L 
    
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    
    def how_many(self, listened_people):
        s = 0
        for name in listened_people :
            if name.lower() not in L :
                L.append(name.lower())
                s+=1
        return s
class Dictionary():
    def __init__(self):
        self.dic = dict()
        
    def newentry(self, word, definition):
        self.dic[word] = definition
        
    def look(self, key):
        if key not in self.dic :
            return f"Can't find entry for {key}"
        return self.dic[key]
class MagicDictionary:
    def __init__(self):
        self.mdictionary = dict()

    def buildDict(self, dictionary: list[str]) -> None:
        for w in dictionary:
            for i, x in enumerate(w):
                possible = w[:i] + '_' + w[i + 1:]
                #mdictionary has keys of every element of dictionary with every way a single character can be replaced by '_'
                if possible in self.mdictionary:
                    #if a key appears twice or more, since every string is unique by constraints, it means these strings themselves are valid matches (since they can be changed to each other)
                    #self.mdictionary[possible] = (lambda y: True) (not working)
                    self.mdictionary[possible] = True
                else:
                    #each key has value a function which checks if a character is the same as the one that has been replaced (since the word itself is not a valid match to itself)
                    #self.mdictionary[possible] = (lambda y: (y!=x)) (not working)
                    self.mdictionary[possible] = x

    def search(self, searchWord: str) -> bool:
        for i, x in enumerate(searchWord):
            possible = searchWord[:i] + '_' + searchWord[i + 1:]
            #checks if searchWord with every way a single character can be replaced by '_' is a key
            if possible in self.mdictionary:
                #checks if a character can be changed to give a string in dictionary (, i.e., the string in dictionary corresponding to the key is not only searchWord itself)
                #if self.mdictionary[possible](x): (not working)
                if self.mdictionary[possible]!=x:
                    return True
        return False



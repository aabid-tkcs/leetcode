class Encrypter:

    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.dictionary = dictionary
        self.encf = dict()
        #stores the corresponding keys and vaues in the dictionary enf
        for i in range(len(keys)):
            self.encf[keys[i]] = values[i]
        
    def encrypt(self, word1: str) -> str:
        encw = ""
        for i in range(len(word1)):
            #checks if the character is a key and appends the corresponding value if it is
            if word1[i] in self.encf:
                encw = encw + self.encf[word1[i]]
            else:
                return ""
        return encw

    def decrypt(self, word2: str) -> int:
        count = 0
        for w in self.dictionary:
            #checks if an element w in dictionary encrypts to it, i.e., if w is a valid decryption
            if (self.encrypt(w) == word2) and (self.encrypt(w) != ""):
                count += 1
        return count
                
                
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        #definition of val
        val = lambda x: ord(x) - ord('a') + 1
        
        #hash function applied to the rightmost substring of length k
        hashf = sum([(val(s[(len(s)) - (k - x)]) * pow(power, x)) for x in range(0,k)]) % modulo
        #checks if the hash function returns the desired value
        if(hashf == hashValue):
            lsubi = (len(s) - k)
        
        
        pk = pow(power, k)
        for x in range((len(s) - 1) - k, -1, -1):
            hashf = (((hashf * power) + val(s[x])) - (val(s[x + k]) * (pk))) % modulo
            #value of hash function applied to the substring starting one index to the left
            #this is possible since addition/subtraction and multiplication are well-defined in modular arithmetic
            #we have to go right to left since division is not well-defined in modular arithmetic
            if hashf == hashValue:
                lsubi = x
                
        return s[lsubi:lsubi+k]
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s

        return encoded

    def decode(self, s: str) -> List[str]:
        #get in a huge string --> loop through it and find length + '#'

        res = []

        i = 0
        while i < len(s): 
            j = i 
            
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            decoded = s[j+1 : j+1+length]
            res.append(decoded)

            i = j + 1 + length
        
        return res


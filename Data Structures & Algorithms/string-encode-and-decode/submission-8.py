class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        #each string in strs 
        for s in strs:
            encoded += str(len(s))
            encoded += '#'
            encoded += s 
        
        return encoded

    def decode(self, s: str) -> List[str]:
        #list to return original list of strings
        res = []

        #loop through the entire mega string
        i=0
        while i < len(s):
            decoded = ""
            j = i 
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            decoded = s[j+1 : j+1+length]
            res.append(decoded)

            i = j + 1 + length 
        
        return res

            


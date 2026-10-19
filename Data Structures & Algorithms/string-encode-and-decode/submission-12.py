class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += str(len(s))
            encoded += '#'
            encoded += s
        
        return encoded #"".join()

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            decoded = s[j+1:j+length+1]
            res.append(decoded)
            i = j+length+1
        
        return res
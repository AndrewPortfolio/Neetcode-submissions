class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []

        i = j = 0
        while i < len(s):
            print("i", i)
            j = i
            print("updated j", j)
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded = s[j+1:j+length+1]
            res.append(decoded)
            
            i = j+length+1
        return res
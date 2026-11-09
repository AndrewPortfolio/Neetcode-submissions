class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, window = {}, {}

        # count chars in t
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        need, have = len(countT), 0
        res, resLen = [-1,-1], float("Infinity")

        i = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if resLen > j-i+1:
                    resLen = j-i+1
                    res = [i,j]
                
                window[s[i]] = window.get(s[i]) - 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
        
        i,j = res

        return s[i:j+1] if resLen != float("Infinity") else ""
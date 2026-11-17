class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        need = len(countT)
        have = 0
        
        res, resLen = [-1, -1], float("Infinity")

        i = 0
        j = i
        while j < len(s):
            c = s[j]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if resLen > j-i+1:
                    res = [i,j]
                    resLen = j-i+1
                
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -=1
                i += 1

            j += 1
        
        i, j = res
        
        return s[i:j+1] if resLen != float("Infinity") else ""
class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if len(s) < len(t):
            return ""
        
        countWin, countT = {}, {}

        for c in t:
            countT[c] = 1+countT.get(c, 0)
        
        have, need = 0, len(countT)

        res, resLen = [-1,-1], float("infinity")

        i = 0
        for j in range(len(s)):
            a = s[j]
            countWin[a] = countWin.get(a, 0) + 1
            
            if a in countT and countWin[a] == countT[a]:
                have += 1
            
            while have == need:
                if j-i+1 < resLen:
                    res = [i, j]
                    resLen = j-i+1

                countWin[s[i]] -= 1
                if s[i] in countT and countWin[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
                
            
        i, j = res

        return s[i:j+1] if resLen != float("infinity") else ""



        
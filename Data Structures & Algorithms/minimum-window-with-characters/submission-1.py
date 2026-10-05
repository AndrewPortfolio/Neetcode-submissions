class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            countT[c] = 1+countT.get(c, 0)
        

        have, need = 0, len(countT)
        i = 0
        res, resLen = [-1, -1], float("infinity")

        for j in range(len(s)):
            c = s[j]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #updates result 
                if (j - i + 1) < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
            
        i, j = res

        return s[i:j+1] if resLen != float("infinity") else ""

            


            

            
            


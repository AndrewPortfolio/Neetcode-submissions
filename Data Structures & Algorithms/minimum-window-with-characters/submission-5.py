class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #store unique chars in t, store chars in curr window
        countT, window = {}, {}

        #count unique chars
        for c in t:
            countT[c] = 1+countT.get(c, 0)
        
        #chars we need, chars we have in window
        need, have = len(countT), 0

        #valid windows
        res, resLen = [-1,-1], float("infinity")

        i=0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1+window.get(c,0)
            if c in countT and window[c] == countT[c]:
                have += 1

            #valid sub-string
            while have == need:
                if j - i + 1 < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                i += 1
        
        i, j = res

        return s[i:j+1] if resLen != float("infinity") else ""
                







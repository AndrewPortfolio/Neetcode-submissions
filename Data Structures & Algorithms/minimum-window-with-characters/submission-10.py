class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}
        
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        
        need = len(count_t)
        have = 0

        res = [-1,-1]
        resLen = float("infinity")

        i = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1 + window.get(c, 0)
            
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if resLen > j-i+1:
                    resLen = j-i+1
                    res = [i,j]
                
                window[s[i]] -= 1
                if s[i] in count_t and window[s[i]] < count_t[s[i]]:
                    have -= 1
                i += 1

        i, j = res
        
        return s[i:j+1] if resLen != float("infinity") else ""
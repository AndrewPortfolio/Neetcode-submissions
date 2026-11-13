class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # {key: A-Z, value: count}
        window = {} 
        maxLen = 0


        i = 0
        for j in range(len(s)):
            c = s[j]
            window[c] = 1 + window.get(c, 0)
            maxf = max(window.values())

            while j-i+1 - maxf > k: 
                window[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j-i+1)
        
        return maxLen
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxL = 0

        i = 0
        for j in range(len(s)):
            window[s[j]] = 1 + window.get(s[j], 0)

            maxF = max(window.values())

            while j-i+1-maxF > k:
                window[s[i]] -= 1
                i += 1
            
            maxL = max(maxL, j-i+1)

        return maxL
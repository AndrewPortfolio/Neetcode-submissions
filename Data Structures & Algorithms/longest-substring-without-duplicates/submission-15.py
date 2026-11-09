class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0

        i = 0
        for j in range(len(s)): 
            c = s[j]
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            seen[c] = j
            maxLength = max(maxLength, j-i+1)

        return maxLength

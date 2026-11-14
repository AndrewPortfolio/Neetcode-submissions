class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxL = 0

        i = 0
        for j in range(len(s)):
            if s[j] in seen:
                i = max(seen[s[j]]+1, i)
            
            seen[s[j]] = j

            maxL = max(maxL, j-i+1)

        return maxL

            
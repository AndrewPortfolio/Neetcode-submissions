class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        i = 0
        maxLength = 0

        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]]+1, i)
            mp[s[j]] = j
            maxLength = max(maxLength, j-i+1)
        return maxLength
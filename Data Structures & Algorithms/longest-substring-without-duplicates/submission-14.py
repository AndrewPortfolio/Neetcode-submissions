class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxLength = 0

        i = 0
        for j in range(len(s)): 
            c = s[j]
            while c in seen:
                seen.remove(s[i])
                i += 1
            seen.add(c)
            maxLength = max(maxLength, j-i+1)

        return maxLength

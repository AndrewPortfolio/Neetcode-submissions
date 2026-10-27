class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        
        maxLength = 1
        seen = set()

        i,j = 0, 1
        seen.add(s[i])

        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                maxLength = max(maxLength, len(seen))
                j += 1
                continue
            else: 
                seen.remove(s[i])
                i += 1
        return maxLength
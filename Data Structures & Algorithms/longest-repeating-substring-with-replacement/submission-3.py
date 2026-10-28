class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        i = 0
        maxF = 0
        for j in range(len(s)):
            count[s[j]] = 1+count.get(s[j], 0)
            maxF = max(maxF, count[s[j]])

            while (j-i+1) - maxF > k:
                count[s[i]] = count.get(s[i]) - 1
                i += 1
            
            res = max(j-i+1,res)

        return res
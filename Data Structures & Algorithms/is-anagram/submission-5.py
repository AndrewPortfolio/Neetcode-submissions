class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen1 = Counter(s)
        seen2 = Counter(t)

        # for i in range(len(s)):
        #     if s[i] not in seen1: 
        #         seen1.add(s[i])
        #     if t[i] not in seen2: 
        #         seen2.add(t[i])
        
        return seen1 == seen2
        


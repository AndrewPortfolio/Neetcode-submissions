class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = Counter(s)
        seen2 = Counter(t)

        # if len(s) != len(t):
        #     return False

        # for i in range(len(s)):
        #     if s[i] not in seen1: 
        #         seen1.add(s[i])
        #     if t[i] not in seen2: 
        #         seen2.add(t[i])
        
        if seen1 == seen2:
                return True 
        
        return False


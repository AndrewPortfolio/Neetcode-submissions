class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Count the occurences of each char in both strings 
        #if they are the same then count should be 0 
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for cnt in count:
            if cnt != 0:
                return False 
        
        return True 

        
        
        #return Counter(s) == Counter(t)
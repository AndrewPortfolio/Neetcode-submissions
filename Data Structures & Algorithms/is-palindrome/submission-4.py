class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = s.lower() 
        s_clean = "".join(filter(str.isalnum, s_clean))
        print(s_clean)


        i = 0
        j = len(s_clean) - 1

        #1 pointer at the beginning and another at the end 
        #if at any point s_clean[i] and s_clean[j] don't equal each other 
        #return false otherwise keep checking 
        #increment i decrement j
        while i <= j:
            if s_clean[i] != s_clean[j]:
                return False

            i += 1
            j -= 1
        
        return True


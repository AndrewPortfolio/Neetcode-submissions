class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        # to track chars we need and what we have in the window
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        

        # track what chars we have and how many we need
        have, need = 0, len(countT)        

        #to track the shortest substring 
        res, resLen = [-1,-1],float("infinity")
        
        #find the smallest substring that contains t
        i = 0 
        for j in range(len(s)):
            a = s[j] 
            window[a] = 1 + window.get(a, 0)
            
            if a in countT and window[a] == countT[a]:
                have += 1
            
            #when substring contains all t chars
            while have == need:
                if j - i + 1 < resLen:
                    res = [i, j]
                    resLen = j - i + 1
                
                #decrement the window count so that we shift left pointer right 
                window[s[i]] -= 1
                if s[i] in countT and window[s[i]] < countT[s[i]]:
                    have -= 1
                
                #shift the window right one
                i += 1
                
        i,j = res

        return s[i : j+1] if resLen != float("infinity") else ""
                

                


                


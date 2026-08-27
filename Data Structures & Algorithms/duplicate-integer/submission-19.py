class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if there is a duplicate return true 
        #ds to store the seen values, if another value inside nums is alr in seen then return true 

        #empty arr
        seen = []

        for n in nums:
            if n in seen:
                return True 
            seen.append(n)
        
        return False
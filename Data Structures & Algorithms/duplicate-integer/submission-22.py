class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #if there is a duplicate return true 
        #ds to store the seen values, if another value inside nums is alr in seen then return true 

        #empty arr
        seen = set()

        for n in nums:
            if n in seen:
                return True 
            seen.add(n)
        
        return False
        #return len(set(nums)) != len(nums)
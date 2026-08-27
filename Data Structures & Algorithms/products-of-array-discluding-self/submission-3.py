class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #compute prefix --> compute postfix 

        res = [0] * len(nums)

        # nums: [1,2,4,6]
        #res: [1,1,2,8]
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        # nums: [1,2,4,6]
        #res: [48,24,12,8]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix 
            postfix *= nums[j]
        
        return res

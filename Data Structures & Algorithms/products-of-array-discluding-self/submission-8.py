class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        #compute product before each index
        prefix = 1
        for i, n in enumerate(nums):
            res[i] = (prefix)
            prefix *= n
        
        # compute the postfix 
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix 
            postfix *= nums[j]
        

        return res

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)

        #at each index compute the product of numbers before it
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]

        #at each index compute the product of numbers after it 
        postfix = 1
        for j in range(len(nums)-1, -1, -1): 
            res[j] *= postfix
            postfix *= nums[j]

        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Return array of products except for itself 
        
        #a list of 0's length of nums
        res = [0] * len(nums)

        #prefix 
        #nums = [1,2,3,4]
        #res = [1,1,2,6]
        prefix = 1
        for i in range(len(nums)): 
            res[i] = prefix 
            prefix *= nums[i]

        #postfix
        #nums = [1,2,3,4]
        #res = [24,12,8,6]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix 
            postfix *= nums[j]
    
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #return prodcut of array except itself 
        res = [0] * len(nums) 

        #prefix = product of all nums before curr num
        #nums = [1,2,4,6]
        #res = [1,1,2,8]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        #postfix = product of all nums after curr num
        #nums = [1,2,4,6]
        #res = [1,1,2,8]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix 
            postfix *= nums[j]

        return res
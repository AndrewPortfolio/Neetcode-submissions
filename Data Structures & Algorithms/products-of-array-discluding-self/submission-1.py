class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #given an int array 
        #return arr output where output[i] == the product of the rest of the elements in the array (not itself)
        #compute the prefix and postfix (think product of nums behind the element, times proudct of nums ahead of the element)

        res = [0] * len(nums)

        #compute prefix --> store into res
        #nums:[1,2,3,4]
        #res: [1,1,2,6]
        prefix = 1
        for i in range(len(nums)):
                res[i] = prefix 
                prefix *= nums[i]

        ##nums:[1,2,3,4]
        #res: [1,1,2,6]
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j] * postfix
            postfix *= nums[j]

        return res
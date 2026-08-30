class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #find the 3 numbers that add up to 0 
        
        nums.sort()

        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue 

            k = i + 1
            j = len(nums)-1
            while k < j:
                threeSum = n + nums[k] + nums[j]
                if threeSum > 0: 
                    j -= 1
                elif threeSum < 0:
                    k += 1
                else: 
                    res.append([n,nums[k],nums[j]])
                    k += 1
                    while nums[k] == nums[k-1] and k < j:
                        k += 1

        return res 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            k = i + 1
            j = len(nums) - 1
            if i > 0 and a == nums[i-1]:
                continue

            while k < j:
                threeSum = a + nums[k] + nums[j]
                if threeSum < 0:
                    k += 1
                elif threeSum > 0:
                    j -= 1
                else:
                    res.append([a,nums[k],nums[j]])
                    k += 1
                    j -= 1
                    while nums[k] == nums[k-1] and k < j:
                        k += 1
                
                
            
        return res
 
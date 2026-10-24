class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)): 
            k, j = i+1, len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while k < j:
                tSum = nums[i] + nums[k] + nums[j] 
                if tSum == 0:
                    res.append([nums[i], nums[k], nums[j]])
                    k += 1
                    j -= 1
                    while k < j and nums[k] == nums[k-1]:
                        k += 1
                    # while k < j and nums[j] == nums[j + 1]:
                    #     j -= 1

                elif tSum > 0:
                    j -= 1
                else:
                    k += 1
            
                

        return res 
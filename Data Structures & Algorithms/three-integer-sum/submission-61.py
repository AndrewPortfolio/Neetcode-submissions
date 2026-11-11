class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            k = i + 1
            j = len(nums) - 1

            if i > 0 and a == nums[i-1]:
                continue

            while k < j:
                tSum = a + nums[k] + nums[j]

                if tSum == 0:
                    res.append([a, nums[k], nums[j]])
                    k+=1
                    while k < j and nums[k] == nums[k-1]:
                        k+=1
                elif tSum < 0:
                    k += 1
                else:
                    j -= 1

        return res 
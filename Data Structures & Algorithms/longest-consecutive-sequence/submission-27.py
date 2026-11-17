class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxL = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
                length = 1
                while nums[i]+length in seen:
                    length += 1
                
                maxL = max(maxL, length)
        

        return maxL
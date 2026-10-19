class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                res = [seen[diff],i]
                break 
            seen[nums[i]] =i 
        
        return res
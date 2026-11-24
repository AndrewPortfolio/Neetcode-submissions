class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #{key: num value: index}
        seen = {}
        res = [-1,-1]

        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                res = [seen[complement], i]
            seen[n] = (i)
        
        return res
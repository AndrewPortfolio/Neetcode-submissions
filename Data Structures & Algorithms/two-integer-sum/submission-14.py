class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sum of 2 numbers = target --> target - a number = a number

        seen = {}

        #{key: nums val: index}
        for i, n in enumerate(nums): 
            complement = target - n 
            if complement in seen:
                return [seen[complement], i]
            
            seen[n] = i

            
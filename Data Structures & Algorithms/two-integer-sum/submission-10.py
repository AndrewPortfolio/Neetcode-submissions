class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        #empty dictionary 
        seen = {}

        #enumerate(nums) gives list of nums with corresponding index 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                #return index where complement lives and i
                return [seen[complement], i]
            #if not seen store the new number in seen with i 
            seen[n] = i
        


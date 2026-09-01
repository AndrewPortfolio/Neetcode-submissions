class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store each number in a seen
        seen = set(nums)
        longest = 0

        for n in nums:
            if n-1 in seen:
                continue 
            length = 0
            while (n + length) in seen:
                length += 1
            
            longest = max(length, longest)

        return longest
        


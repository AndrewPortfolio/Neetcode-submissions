class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1 

        i, j = 0, len(nums)-1 

        while i <= j:
            m = (i+j) // 2
            if nums[m] == target:
                return m

            # [9,4,5,6,7,8]
            #lhs of sort 
            if nums[i] <= nums[m]:
                if target > nums[m] or target < nums[i]:
                    i = m + 1 
                else:
                    j = m - 1
            #rhs of sort 
            else: 
                if target < nums[m] or target > nums[j]:
                    j = m - 1
                else:
                    i = m + 1
            
        return res 
              
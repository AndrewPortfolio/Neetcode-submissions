class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1

        while i <= j:
            m = (i + j) // 2
            if nums[m] == target:
                return m

            #check if left side is sorted
            if nums[i] <= nums[m]:
                #if target lives within the left most number and the middle 
                if nums[i] <= target < nums[m]:
                    # search left
                    j = m - 1
                else:
                    #search right 
                    i = m + 1
            #right side is sorted
            else: 
                #target is within the sorted right side
                if nums[m] < target <= nums[j]:
                    #search rigth
                    i = m + 1

                #target isn't in right side
                else:
                    #search left
                    j = m - 1
        return -1
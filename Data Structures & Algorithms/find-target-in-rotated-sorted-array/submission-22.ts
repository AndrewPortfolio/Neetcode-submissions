class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {    
        let i = 0,
            j = nums.length-1
        let res = -1

        while (i <= j) {
            let m = Math.trunc((i+j)/2)
            if (nums[m] === target) {
                res = m
                break
            }
            
            if (nums[i] <= nums[m]) { //means lhs is sorted
                if (nums[i] <= target && target <= nums[m]) { //if target is between i and 
                    j = m-1
                }
                else {
                    i = m+1
                }
            }
            else {
                if (nums[m] <= target && target <= nums[j]) {
                    i = m + 1
                }
                else {
                    j = m-1
                }
            }
        }


        return res
    }
}

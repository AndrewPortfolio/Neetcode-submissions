class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums: number[]): number {
        let res = nums[0]
        let i = 0
        let j = nums.length - 1

        while (i <= j) {
            if (nums[i] < nums[j]) {
                res = Math.min(res, nums[i])
                break 
            }
            const m = Math.trunc((i+j) / 2) // integer division
            res = Math.min(res, nums[m])

            if(nums[i] <= nums[m]) { // lhs is sorted in ascending order 
                i = m + 1
            }
            else {
                j = m - 1 
            }

        }

        return res 
    }
}

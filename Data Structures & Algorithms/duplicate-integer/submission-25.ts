class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const nSet = new Set(nums)
        return nums.length != nSet.size
    }
}

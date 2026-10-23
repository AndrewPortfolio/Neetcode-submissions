class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        const length = nums.length
        const res = new Array(length).fill([0])

        // compute the prefix for each index
        let prefix = 1
        for (let i = 0; i < length; i++) {
            res[i] = prefix
            prefix *= nums[i]
        }

        // posfix
        let postfix = 1
        for (let j = length-1; j >= 0; j--) {
            res[j] *= postfix
            postfix *= nums[j]
        }

        return res
    }
}

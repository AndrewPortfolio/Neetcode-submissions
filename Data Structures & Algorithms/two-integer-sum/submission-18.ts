class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const seen = new Map<number, number>

        const res = []
        for (let i = 0; i < nums.length; i++){
            let diff = target - nums[i]
            if (seen.has(diff)) {
                // let res = [seen[diff], i]
                res.push(seen.get(diff))
                res.push(i)
            }
            seen.set(nums[i], i)
        }
        return res
    }
}

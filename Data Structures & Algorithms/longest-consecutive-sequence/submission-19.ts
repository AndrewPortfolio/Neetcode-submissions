class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const unqNums = new Set<number>();
        let maxCon = 0

        for (const n of nums) {
            unqNums.add(n)
        }

        for (let i = 0; i < nums.length; i++) {
            let length = 1
            if (!unqNums.has(nums[i]-1)) {
                while (unqNums.has(nums[i] + length)) {
                    length++
                }
            }
            maxCon = Math.max(maxCon, length)
        }

        return maxCon 
    }
}

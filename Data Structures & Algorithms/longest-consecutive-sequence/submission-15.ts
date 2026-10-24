class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const numList = new Set<number>(nums)
        let longest = 0

        for (const n of numList) {
            if (!numList.has(n-1)) { 
                let length = 1
                while (numList.has(n+length)) {
                    length += 1
                }

                longest = Math.max(length, longest)
            }
        }

        return longest 
    }
}

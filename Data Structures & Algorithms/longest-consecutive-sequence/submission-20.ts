class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const seen = new Set<number>(nums);
        let maxLength = 0;

        // for (const n of nums) {
        //     seen.add(n); 
        // }

        for (let i = 0; i < nums.length; i++){
            if (!seen.has(nums[i]-1)) {
                let length = 1;
                while (seen.has(nums[i] + length)) {
                    length++;
                }
                maxLength = Math.max(maxLength, length);
            }
        }
        return maxLength;
    }
}

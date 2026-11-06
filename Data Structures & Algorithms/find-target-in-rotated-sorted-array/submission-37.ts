class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let res = -1;

        let i = 0;
        let j = nums.length - 1;
        while (i <= j) {
            const m = Math.trunc((j+i) / 2);
            if (nums[m] === target) {
                res = m;
            }

            if (nums[i] <= nums[m]) { // in left side sorted portion
                if (nums[i] <= target && target <= nums[m]) { // target lives on left side
                    j = m - 1;
                }
                else { // target on right side
                    i = m + 1;
                }
            }
            else { // in right side sorted portion
                if (nums[m] <= target && target <= nums[j]) {
                    i = m + 1;
                }
                else {
                    j = m - 1;
                }
            }
        }

        return res;
    }
}
 
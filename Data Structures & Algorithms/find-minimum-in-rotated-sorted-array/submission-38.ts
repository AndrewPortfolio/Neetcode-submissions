class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums: number[]): number {
        let min = nums[0];

        let i = 0,
            j = nums.length - 1;
        
        while (i <= j) {
            if (nums[i] <= nums[j]) {
                min = Math.min(min, nums[i]);
                break;
            }

            let m = i + Math.trunc((j-i) / 2);
            min = Math.min(min, nums[m]);

            if (nums[m] >= nums[i]) {
                i = m+1;
            }
            else {
                j = m-1;
            }

        }

        return min;
    }
}
 
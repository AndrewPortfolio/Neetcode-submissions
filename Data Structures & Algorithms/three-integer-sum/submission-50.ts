class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][]{
        nums.sort((a,b) => a-b);
        const res = [];

        for (let i = 0; i < nums.length; i++) {
            const a = nums[i];
            if(a > 0) break;

            if (i > 0 && a === nums[i-1]) {
                continue
            }

            let k = i + 1;
            let j = nums.length - 1;
            while (k < j) {
                const tSum = a + nums[k] + nums[j];
                if (tSum === 0) {
                    res.push([a, nums[k], nums[j]])
                    k++
                    j--

                    while (k < j && nums[k] === nums[k-1]) {
                        k++
                    }
                }
                else if (tSum > 0) {
                    j--
                }
                else {
                    k++
                }
                
            }
        }

        return res
    }
}

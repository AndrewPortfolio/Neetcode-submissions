class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        const res = [];
        nums = nums.sort((a,b) => a-b);
        console.log(nums)

        for (let i = 0; i < nums.length; i++) {
            const a = nums[i];
            let k = i + 1;
            let j = nums.length-1;

            if (i > 0 && nums[i-1] === nums[i]) {
                continue;
            }

            while (k < j) {
                const tSum = a + nums[k] + nums[j];
                if (tSum === 0) {
                    res.push([a,nums[k],nums[j]])
                    k++;
                    while (k < j && nums[k-1] === nums[k]) {
                        k++;
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
        return res; 
    }
}

class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        const res = []
        nums.sort((a,b) => a-b)

        for (let i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                break 
            }

            if (i > 0 && nums[i] === nums[i-1]) {
                continue 
            }

            let k = i + 1
            let j = nums.length - 1
            while (k < j) {
                let tSum = nums[i] + nums[k] + nums[j]
                if (tSum === 0) {
                    res.push([nums[i], nums[k], nums[j]])
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

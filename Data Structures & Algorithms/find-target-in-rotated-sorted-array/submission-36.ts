class Solution {
    search(nums: number[], target: number): number {
        let res = -1
        let i = 0,
            j = nums.length-1
        
        while (i <= j) {
            console.log("i", i, "j",j)
            const m = i + Math.trunc((j-i) / 2)
            console.log("index", m, "num",nums[m])
            
            if (nums[m] === target) {
                return m
            }

            // find which side is sorted
            if (nums[i] <= nums[m]) { //left side is
                if(nums[i] <= target && target < nums[m]) { //target loc in range i-m
                    j = m-1
                }
                else {
                    i = m+1
                }
            }
            else { // right side is
                if (nums[m] < target && target <= nums[j]) {
                    i = m+1
                }
                else {
                    j = m-1
                }
            }
        }

        return res
    }
}

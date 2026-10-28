class Solution {
    findMin(nums: number[]): number {
        let i = 0,
            j = nums.length - 1;
        
        while (i < j) {
            let m = i + Math.trunc((j-i) / 2);
           
            if (nums[m] < nums[j]) { 
                // smaller values are on left side
                j = m 
            }
            else {
                //smaller values are on the right side
                i = m + 1
            }     
        }

        return nums[i]
    }
}

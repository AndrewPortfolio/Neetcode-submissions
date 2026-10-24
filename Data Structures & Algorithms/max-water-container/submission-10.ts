class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights: number[]): number {
        let i = 0
        let j = heights.length - 1
        let maxA = 0

        while (i < j) {
            const height = Math.min(heights[i], heights[j])
            const width = j - i
            const area = height * width 

            maxA = Math.max(area, maxA)

            if (heights[i] < heights[j]) {
                i++
            } else {
                j--
            }
        }

        return maxA
    }
}

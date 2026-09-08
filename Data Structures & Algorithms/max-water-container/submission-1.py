class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0 

        i = 0
        j = len(heights)-1
        while i < j:
            width = j-i
            height = min(heights[i], heights[j])
            area = height * width
            print(area)
            maxA = max(maxA , area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxA

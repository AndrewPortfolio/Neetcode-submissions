class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1 
        maxA = 0 

        while i < j:
            l = j - i 
            #print(f'length: {l}')
            h = min(heights[i], heights[j])
            #print(f'height {h}')
            area = l * h 
            # print(f'Area {area}')

            maxA = max(area, maxA)
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxA
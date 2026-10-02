class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0 

        i, j = 0, 1
        while j < len(prices):
            profit = prices[j] - prices[i]
            maxP = max(maxP, profit)

            if prices[i] > prices[j]:
                i = j
            j += 1
        
        return maxP
        
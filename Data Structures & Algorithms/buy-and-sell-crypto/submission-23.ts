class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let maxP = 0

        let i = 0,
            j = 0
        
        while (j < prices.length-1) {
            maxP = Math.max(maxP, prices[j]-prices[i])
            if (prices[i] > prices[j] && i < j) {
                i++
            }
            else {
                j++
            }

            maxP = Math.max(maxP, prices[j]-prices[i])
            console.log("Calc:", prices[j]-prices[i])
            console.log("Max", maxP)


        }


        return maxP 
    }
}

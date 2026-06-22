class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6,7,1]
        
        maxProfit = 0
        buy = prices[0]
        
        for sell in prices:
            profit = sell - buy
            maxProfit = max(maxProfit, profit)
            buy = min(sell, buy) #update lowest buy for future iteration
        
        return maxProfit
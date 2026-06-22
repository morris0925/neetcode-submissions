class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[10,1,5,6,7,1]
        
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else: #跟 "l" 比找有沒有更小
                l = r
            
            r += 1

        return maxProfit
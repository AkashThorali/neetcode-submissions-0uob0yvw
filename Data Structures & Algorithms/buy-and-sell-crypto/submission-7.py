class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0

        maxProfit = 0
        while r < len(prices) - 1: 
            r +=  1
            if prices[l] > prices[r]: 
                l = r
            else: 
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)

        return maxProfit



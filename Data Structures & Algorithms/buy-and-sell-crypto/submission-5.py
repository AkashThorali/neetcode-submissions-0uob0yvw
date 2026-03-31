class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        for i in range(len(prices) - 1):
            stock_to_buy = prices[i]
            window = i + 1

            while window < len(prices): 
                if prices[window] > stock_to_buy: 
                    profit = prices[window] - stock_to_buy
                    maxProfit = max(maxProfit, profit)
                window += 1
        return maxProfit




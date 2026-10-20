class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        max_profit = 0
        best_buy = prices[0]
        
        for i in prices[1:]: # starts from 1st index
            max_profit = max(max_profit, i - best_buy) # checks which is greater, our current max_profit or the new value
            best_buy = min(best_buy, i) # which is lower price

        return max_profit

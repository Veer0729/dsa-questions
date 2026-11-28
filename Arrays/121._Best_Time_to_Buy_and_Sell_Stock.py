class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        buy = prices[0] # we start from buying the 1st element
        max_profit = 0 # current profit is 0

        for i in prices: # for every price in our list
            if i < buy: # if this new num is smaller than our current buy
                buy = i # we replace it
            elif i - buy > max_profit: # but if that num - our buying price is greater than our profit
                max_profit = i - buy # our max profit is this new value
        return max_profit

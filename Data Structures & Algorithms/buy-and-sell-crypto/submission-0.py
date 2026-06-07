class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy  = prices[0]
        profit = 0
        for _ ,stock in enumerate(prices):
            profit = max(profit , stock - buy)
            if buy > stock:
                buy = stock
        return profit
    

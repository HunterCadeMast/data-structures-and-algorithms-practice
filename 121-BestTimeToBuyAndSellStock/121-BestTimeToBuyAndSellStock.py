# Last updated: 2/12/2026, 3:45:37 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for sell in prices:
            if sell < buy:
                buy = sell
            elif sell - buy > profit:
                profit = sell - buy
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float('inf')
        max_profit = 0

        for price in prices:
            minimum_price = min(minimum_price, price)
            max_profit = max(max_profit, price - minimum_price)
        return max_profit
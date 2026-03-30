class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Algorithm: Buy low, sell high
        # We want to minimize buy prize, and maximize sell price 
        
        max_profit = 0

        buy_price = prices[0]
        for i in range(1, len(prices)):
            # Calculating current profit
            cur_profit = prices[i] - buy_price 
            max_profit = max(max_profit, cur_profit)

            # Seeing lowest price so far
            buy_price = min(buy_price, prices[i])

        return max_profit
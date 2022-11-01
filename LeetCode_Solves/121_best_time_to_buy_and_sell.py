class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        n=len(prices)
        for i in range(n):
            if buy_price<prices[i]:
                curr_price=-buy_price+prices[i]
                profit=max(profit,curr_price)
            else:
                buy_price=prices[i]
        return profit
            
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         dp = [0] * len(prices)
#         cheapest = prices[0]
#         for i in range(1, len(prices)):
#             cheapest = min(cheapest, prices[i])
#             if prices[i] > cheapest:
#                 dp[i] = max(dp[i - 1], prices[i] - cheapest)
#             else:
#                 dp[i] = dp[i - 1]

#         return dp[-1]
    
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = 10000
        profit = 0
        for price_current in prices:
            price_min = min(price_current, price_min)
            profit = max(profit, price_current-price_min)
        return profit
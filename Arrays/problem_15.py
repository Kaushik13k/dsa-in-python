# Best time to buy and sell stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        minPrice = float("inf")
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            maxPro = max(maxPro, prices[i] - minPrice)
        return maxPro

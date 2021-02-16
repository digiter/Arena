# 123. Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell = [0] * n
        minPrice = prices[0]
        for x in range(n):
            sell[x] = prices[x] - minPrice
            minPrice = min(minPrice, prices[x])

        prefixMax = [sell[0]] * n
        for x in range(1, n):
            prefixMax[x] = max(sell[x], prefixMax[x - 1])

        buy = [0] * n
        maxPrice = prices[-1]
        for x in range(n - 1, -1, -1):
            buy[x] = maxPrice - prices[x]
            maxPrice = max(maxPrice, prices[x])

        suffixMax = [buy[-1]] * n
        for x in range(n - 2, -1, -1):
            suffixMax[x] = max(buy[x], suffixMax[x + 1])

        # Buy and sell only once.
        ans = prefixMax[n - 1]
        for x in range(1, n):
            # Buy and sell twice.
            ans = max(ans, prefixMax[x - 1] + suffixMax[x])
        return ans

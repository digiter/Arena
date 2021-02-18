# 188. Best Time to Buy and Sell Stock IV
# O(k * n), 136 ms
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0] * (n + 5) for _ in range(k + 5)]
        oldAns = None
        for x in range(1, k + 1):
            maxPrevious = 0 + -prices[0]
            for y in range(1, n):
                dp[x][y] = dp[x][y - 1]
                # Does not sell at prices[y].
                dp[x][y] = max(dp[x][y], dp[x - 1][y])
                # Sells at prices[y].
                dp[x][y] = max(dp[x][y], maxPrevious + prices[y])

                maxPrevious = max(maxPrevious, dp[x - 1][y - 1] + -prices[y])

            if not oldAns or oldAns < dp[k][n - 1]:
                oldAns = dp[k][n - 1]
            else:
                return dp[k][n - 1]

        return dp[k][n - 1]

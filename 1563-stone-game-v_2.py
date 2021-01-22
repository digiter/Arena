# 1563. Stone Game V
# Time: O(N^2), 5280 ms	
#
# Another bottom up dynamic programming.
# Loops y increasing and x decreasing, in order to enumerate interval [x, y] from small to large.
# So that the answer of interval [x, y] can be constructed via its sub-intervals.

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        stoneValue.insert(0, 0)  # Makes it one-based.

        prefixSum = [0] * (N + 1)
        for i in range(1, N + 1):
            prefixSum[i] = prefixSum[i - 1] + stoneValue[i]

        def rangeSum(begin, end):
            return prefixSum[end] - prefixSum[begin - 1]

        dp = [[0] * (N + 1) for _ in range(N + 1)]
        leftBest = copy.deepcopy(dp)
        rightBest = copy.deepcopy(dp)

        for y in range(1, N + 1):
            dp[y][y] = 0
            leftBest[y][y] = 0 + stoneValue[y]
            rightBest[y][y] = 0 + stoneValue[y]
            cut = y
            for x in range(y - 1, 0, -1):
                while x <= cut - 1 and rangeSum(x, cut - 1) >= rangeSum(cut, y):
                    cut -= 1

                def tryUse(t):
                    if not (x <= t - 1 and t <= y):
                        return
                    diff = rangeSum(x, t - 1) - rangeSum(t, y)
                    if diff < 0:
                        dp[x][y] = max(dp[x][y], leftBest[x][t - 1])
                    elif diff == 0:
                        dp[x][y] = max(dp[x][y], leftBest[x][t - 1], rightBest[t][y])
                    else:
                        dp[x][y] = max(dp[x][y], rightBest[t][y])

                tryUse(cut)
                tryUse(cut + 1)

                leftBest[x][y] = max(leftBest[x][y - 1], rangeSum(x, y) + dp[x][y])
                rightBest[x][y] = max(rightBest[x + 1][y], rangeSum(x, y) + dp[x][y])

        return dp[1][N]

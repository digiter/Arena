# 1563. Stone Game V
# Dynamic programming from bottom up.
# O(N^2)

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
        leftCut = copy.deepcopy(dp)
        leftMax = copy.deepcopy(dp)
        rightCut = copy.deepcopy(dp)
        rightMax = copy.deepcopy(dp)

        # Initializes when size is 1.
        for x in range(1, N + 1):
            dp[x][x] = 0
            leftCut[x][x] = x - 1
            leftMax[x][x] = 0
            rightCut[x][x] = x + 1
            rightMax[x][x] = 0

        for size in range(2, N + 1):
            for begin in range(1, N + 1 - size + 1):
                end = begin + size - 1

                lc = leftCut[begin][end - 1]
                lm = leftMax[begin][end - 1]
                while lc + 1 < end and rangeSum(begin, lc + 1) <= rangeSum(lc + 2, end):
                    lm = max(lm, rangeSum(begin, lc + 1) + dp[begin][lc + 1])
                    lc += 1
                leftCut[begin][end] = lc
                leftMax[begin][end] = lm

                rc = rightCut[begin + 1][end]
                rm = rightMax[begin + 1][end]
                while begin < rc - 1 and rangeSum(rc - 1, end) <= rangeSum(
                    begin, rc - 2
                ):
                    rm = max(rm, rangeSum(rc - 1, end) + dp[rc - 1][end])
                    rc -= 1
                rightCut[begin][end] = rc
                rightMax[begin][end] = rm

                dp[begin][end] = max(lm, rm)

        return dp[1][N]

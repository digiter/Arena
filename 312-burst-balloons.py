# 312. Burst Balloons
# Inspired by https://leetcode.com/problems/burst-balloons/discuss/1071954/Simplest-explanation
# dp[x][y] represents keeping nums[x] and nums[y] but bursting all the ballons between x and y.
# O(n^3)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 5) for _ in range(n + 5)]
        nums = [1] + nums + [1]
        # Loops interval [x, y] from small to large, so that it calculates sub-problems first.
        for y in range(n + 2):
            for x in range(y - 2, -1, -1):
                for m in range(x + 1, y):
                    dp[x][y] = max(
                        dp[x][y], dp[x][m] + dp[m][y] + nums[x] * nums[m] * nums[y]
                    )
        return dp[0][n + 1]

# https://leetcode.com/problems/least-operators-to-express-number/
# O(log(target))
from functools import cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # The cost of +/- x^i
        cost = [0] * 35
        cost[0] = 2  # +/- x/x
        for i in range(1, 35):
            cost[i] = i

        @cache
        def dp(i, cnt):  # The remaining target = x^i * cnt
            if cnt <= x - cnt:
                return cnt * cost[i]
            elif cnt == x:
                return cost[i + 1]
            else:
                quotient, remainder = divmod(cnt, x)
                return min(remainder * cost[i] + dp(i + 1, quotient),
                           (x - remainder) * cost[i] + dp(i + 1, quotient + 1))

        return dp(0, target) - 1

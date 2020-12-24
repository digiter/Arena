# https://leetcode.com/problems/least-operators-to-express-number/
# This is wrong becuase choice2 assumes the cost of an extra x^(i+1) is
# `1+cost[i+1]`. But the minimum cost of x^(i+1) could be using substract
# instead of addtion.
from functools import cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        MAX = 36
        power, cost = [1], [2]  # +/- x^i and its cost
        for i in range(1, MAX):
            power.append(power[i - 1] * x)
            cost.append(i)

        @cache
        def dp(i, goal):
            if i == -1:
                return 0
            if not (power[i] <= goal and goal < power[i + 1]):
                print(i, goal, dp(i - 1, goal))
                return dp(i - 1, goal)
            # goal = quotient * x^i + remainer
            # 1 <= quotient < x
            # 0 <= remainer < x^i
            quotient, remainer = divmod(goal, power[i])
            choice1 = quotient * cost[i]
            choice2 = 1 + cost[i + 1] + (x - quotient) * cost[i]
            print(i, goal, min(choice1, choice2) + dp(i - 1, remainer))
            return min(choice1, choice2) + dp(i - 1, remainer)

        return dp(MAX - 2, target) - 1


if __name__ == "__main__":
    s = Solution()
    print(s.leastOpsExpressTarget(3, 929))  # Outputs 21, expected 19

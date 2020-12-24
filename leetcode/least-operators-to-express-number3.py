# https://leetcode.com/problems/least-operators-to-express-number/
# O(log(target)^2)
from functools import cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        @cache
        def solve(goal):
            if goal == 0:
                return 0
            if x > goal:
                # x/x + x/x + ...
                choice1 = goal + goal - 1
                # x - x/x - x/x - ...
                choice2 = (x - goal) * 2
                return min(choice1, choice2)
            if x == goal:
                return 0
            # Now x < goal
            power, cost = x, 0
            while not (power <= goal and goal < power * x):
                power, cost = power * x, cost + 1

            if goal - power == 0:
                return cost

            # x^i + (goal - power)
            choice1 = cost + 1 + solve(goal - power)
            if goal - power <= power * x - goal:
                # This is due to the fact that when a <= b, solve(a) <= solve(b)
                return choice1
            else:
                # x^(i+1) - (x^(i+1) - goal)
                choice2 = (cost + 1) + 1 + solve(power * x - goal)
                return min(choice1, choice2)

        return solve(target)


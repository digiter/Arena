# 1553. Minimum Number of Days to Eat N Oranges
# Time: O(log(N)) as it always reduces the problem size by 2 or 3, 36 ms

class Solution:
    def minDays(self, n: int) -> int:
        INF = 2 * 10 ** 9 + 5

        @cache
        def solve(x):
            if x <= 2:
                return x

            res = INF
            if x % 3 == 0:
                res = min(res, 1 + solve(x // 3))
            elif x % 3 == 1:
                res = min(res, 2 + solve((x - 1) // 3))
            else:
                res = min(res, 3 + solve((x - 2) // 3))

            if x % 2 == 0:
                res = min(res, 1 + solve(x // 2))
            else:
                res = min(res, 2 + solve((x - 1) // 2))

            return res

        return solve(n)

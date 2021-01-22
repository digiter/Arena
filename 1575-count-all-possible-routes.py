# 1575. Count All Possible Routes

class Solution:
    def countRoutes(
        self, locations: List[int], start: int, finish: int, fuel: int
    ) -> int:
        N = len(locations)
        MOD = 10 ** 9 + 7

        @cache
        def solve(x, leftover):
            res = 1 if x == finish else 0
            for y in range(N):
                if y == x:
                    continue
                cost = abs(locations[x] - locations[y])
                if cost <= leftover:
                    res += solve(y, leftover - cost)
                    res %= MOD
            return res

        return solve(start, fuel)

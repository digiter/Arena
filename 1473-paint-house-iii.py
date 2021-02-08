# 1473. Paint House III
# O(m * n * target * n)

class Solution:
    def minCost(
        self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int
    ) -> int:
        INF = 10 ** 4 * 100 + 5

        isPainted = lambda x: houses[x] != 0

        @cache
        def solve(x, groupCnt, color):
            xCost = 0 if isPainted(x) else cost[x][color - 1]
            if x == 0:
                return xCost if groupCnt == 1 else INF
            if groupCnt == 0:
                return INF

            prev = INF
            if isPainted(x - 1):
                newGroup = 1 if houses[x - 1] != color else 0
                prev = min(prev, solve(x - 1, groupCnt - newGroup, houses[x - 1]))
            else:
                for c in range(1, n + 1):
                    newGroup = 1 if c != color else 0
                    prev = min(prev, solve(x - 1, groupCnt - newGroup, c))
            return xCost + prev

        ans = INF
        if isPainted(m - 1):
            ans = solve(m - 1, target, houses[m - 1])
        else:
            for c in range(1, n + 1):
                ans = min(ans, solve(m - 1, target, c))
        return ans if ans != INF else -1

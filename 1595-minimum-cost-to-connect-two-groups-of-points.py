# 1595. Minimum Cost to Connect Two Groups of Points
# Time: 380 ms

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        size1 = len(cost)
        size2 = len(cost[0])

        greedy = [0] * size2
        for y in range(size2):
            greedy[y] = min(cost[x][y] for x in range(size1))

        # Connects all of G1 to a subset of G2,
        # then greedily connects the remaining items of G2 to G1.
        @cache
        def solve(x, mask):
            if x == size1:
                s = 0
                for y in range(size2):
                    if (mask & (1 << y)) == 0:
                        s += greedy[y]
                return s
            return min(cost[x][y] + solve(x + 1, mask | (1 << y)) for y in range(size2))

        return solve(0, 0)

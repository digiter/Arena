# 174. Dungeon Game

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        inf = 10 ** 9

        # The health before entering (x, y).
        @cache
        def healthBefore(x, y):
            if x == m - 1 and y == n - 1:
                return max(1, 1 - dungeon[m - 1][n - 1])
            if x == m or y == n:
                # Shouldn't go outside the dungeon.
                return inf

            return min(
                max(1, healthBefore(x + 1, y) - dungeon[x][y]),
                max(1, healthBefore(x, y + 1) - dungeon[x][y]),
            )

        return healthBefore(0, 0)

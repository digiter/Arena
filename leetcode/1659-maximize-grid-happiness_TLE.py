# 1659. Maximize Grid Happiness
# This solution got TLE for input (5, 5, 5, 5): it takes 3380 ms to run.
# Time complexity (roughtly):
#   Number of states: 5 * 6 * 6 * 3^5
#   Number of transitions: 3^5 * 5
# So 5*10^7 in total.

class Solution:
    def getMaxGridHappiness(
        self, m: int, n: int, introvertsCount: int, extrovertsCount: int
    ) -> int:
        EMPTY, IN, EX = 0, 1, 2

        def generateRow(inCnt, exCnt, row, colIndex):
            if colIndex == n:
                yield row
                return

            row[colIndex] = EMPTY
            for r in generateRow(inCnt, exCnt, row, colIndex + 1):
                yield r

            if inCnt > 0:
                row[colIndex] = IN
                for r in generateRow(inCnt - 1, exCnt, row, colIndex + 1):
                    yield r

            if exCnt > 0:
                row[colIndex] = EX
                for r in generateRow(inCnt, exCnt - 1, row, colIndex + 1):
                    yield r

        @cache
        def solve(rowIndex, inCnt, exCnt, prevRow):
            if rowIndex == m:
                return 0
            if inCnt == 0 and exCnt == 0:
                return 0

            ans = 0
            for row in generateRow(inCnt, exCnt, [-1] * n, 0):
                score = 0
                nextInCnt, nextExCnt = inCnt, exCnt
                # Accounts score update for the previous row.
                for i in range(n):
                    if prevRow[i] == IN:
                        if row[i] != EMPTY:
                            score -= 30
                    elif prevRow[i] == EX:
                        if row[i] != EMPTY:
                            score += 20
                # Accounts score update for the current row.
                for i in range(n):
                    if row[i] == IN:
                        score += 120
                        if prevRow[i] != EMPTY:
                            score -= 30
                        if 0 <= i - 1 and row[i - 1] != EMPTY:
                            score -= 30
                        if i + 1 < n and row[i + 1] != EMPTY:
                            score -= 30
                        nextInCnt -= 1
                    elif row[i] == EX:
                        score += 40
                        if prevRow[i] != EMPTY:
                            score += 20
                        if 0 <= i - 1 and row[i - 1] != EMPTY:
                            score += 20
                        if i + 1 < n and row[i + 1] != EMPTY:
                            score += 20
                        nextExCnt -= 1
                score += solve(rowIndex + 1, nextInCnt, nextExCnt, tuple(row))
                ans = max(ans, score)
            return ans

        return solve(0, introvertsCount, extrovertsCount, tuple([EMPTY] * n))

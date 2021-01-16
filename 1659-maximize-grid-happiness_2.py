# 1659. Maximize Grid Happiness
#
# Time complexity of this dynamic programming:
#   Number of states: 5^2 * 6 * 6 * 3^5
#   Number of transitions: 3 * 5
# So 3*10^6 in total.
#
# It takes 228 ms to calculate the input of (5, 5, 5, 5).


class Solution:
    def getMaxGridHappiness(
        self, m: int, n: int, introvertsCount: int, extrovertsCount: int
    ) -> int:
        EMPTY, IN, EX = 0, 1, 2

        def connect(x, y):
            delta = 0
            if x == IN and y != EMPTY:
                delta += -30
            if x == EX and y != EMPTY:
                delta += 20
            if y == IN and x != EMPTY:
                delta += -30
            if y == EX and x != EMPTY:
                delta += 20
            return delta

        @cache
        def solve(index, inCnt, exCnt, prevN):
            if index == m * n:
                return 0
            if inCnt == 0 and exCnt == 0:
                return 0

            ansEmpty = solve(index + 1, inCnt, exCnt, prevN[1:] + (EMPTY,))

            ansIn = 0
            if inCnt > 0:
                ansIn += 120
                # Updates the above grid.
                ansIn += connect(prevN[0], IN)
                # Updates the left grid.
                if 1 <= index % n:
                    ansIn += connect(prevN[-1], IN)
                ansIn += solve(index + 1, inCnt - 1, exCnt, prevN[1:] + (IN,))

            ansEx = 0
            if exCnt > 0:
                ansEx += 40
                # Updates the above grid.
                ansEx += connect(prevN[0], EX)
                # Updates the current grid.
                if 1 <= index % n:
                    ansEx += connect(prevN[-1], EX)
                ansEx += solve(index + 1, inCnt, exCnt - 1, prevN[1:] + (EX,))

            return max(ansEmpty, ansIn, ansEx)

        return solve(0, introvertsCount, extrovertsCount, tuple([EMPTY] * n))

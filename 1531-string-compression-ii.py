# 1531. String Compression II
# The dynamic programming states are sparse.

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        char, cnt = [], []
        x = 0
        while x < len(s):
            y = x + 1
            while y < len(s) and s[y] == s[x]:
                y += 1
            char.append(s[x])
            cnt.append(y - x)
            x = y

        INF = 105

        def runLen(count):
            if count <= 1:
                return count
            if count <= 9:
                return 2
            if count <= 99:
                return 3
            return 4

        @cache
        def solve(i, lastChar, lastCnt, remaining):
            if i == len(char):
                return runLen(lastCnt)

            res = INF
            # Tries to remove all of char[i].
            if cnt[i] <= remaining:
                res = min(res, 0 + solve(i + 1, lastChar, lastCnt, remaining - cnt[i]))

            if lastChar == char[i]:
                extra = 0
                lastCnt += cnt[i]
            else:
                extra = runLen(lastCnt)
                lastChar, lastCnt = char[i], cnt[i]
            # Tries to remove to only one, a single digit, or double digits.
            for x in [1, 9, 99]:
                if lastCnt > x and (lastCnt - x) <= remaining:
                    res = min(
                        res,
                        extra + solve(i + 1, lastChar, x, remaining - (lastCnt - x)),
                    )
            # Tries to do nothing to char[i].
            res = min(res, extra + solve(i + 1, lastChar, lastCnt, remaining))
            return res

        return solve(0, "#", 0, k)

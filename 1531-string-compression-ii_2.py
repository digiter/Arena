# 1531. String Compression II
# O(kN^2), 1340 ms	

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
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
        def solve(x, atMost):
            if x == -1:
                return 0

            # Deletes s[x].
            res = INF
            if atMost - 1 >= 0:
                res = solve(x - 1, atMost - 1)

            # Keeps s[x], enumerates the last group that equals s[x].
            cnt = 1
            res = min(res, solve(x - 1, atMost) + runLen(cnt))
            for i in range(x - 1, -1, -1):
                if s[i] == s[x]:
                    cnt += 1
                else:
                    atMost -= 1

                if atMost >= 0:
                    res = min(res, solve(i - 1, atMost) + runLen(cnt))
                else:
                    break

            return res

        return solve(len(s) - 1, k)

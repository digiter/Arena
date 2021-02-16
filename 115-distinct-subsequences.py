# 115. Distinct Subsequences
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def solve(a, b):
            if not a:
                return 1 if not b else 0
            if not b:
                return 1

            if a[-1] == b[-1]:
                return solve(a[:-1], b) + solve(a[:-1], b[:-1])
            else:
                return solve(a[:-1], b)

        return solve(s, t)

# 44. Wildcard Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def solve(x, y):
            if x == -1:
                if y == -1:
                    return True
                else:
                    # Empty s can match a series of stars.
                    return p[y] == "*" and solve(x, y - 1)
            if y == -1:
                return False

            if p[y] == "*":
                # The star matches empty.
                if solve(x, y - 1):
                    return True
                # The star matches s[x].
                if solve(x - 1, y):
                    return True
            elif p[y] == "?" or p[y] == s[x]:
                if solve(x - 1, y - 1):
                    return True
            return False

        return solve(len(s) - 1, len(p) - 1)

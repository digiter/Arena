# 87. Scramble String
# O(30^5), 212 ms

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def solve(a, b, c, d):
            if b - a == 0:
                return True
            if b - a == 1:
                return s1[a] == s2[c]

            # Same order: [a, a+i), [a+i, b), [c, c+i), [c+i, d)
            for i in range(1, b - a):
                if solve(a, a + i, c, c + i) and solve(a + i, b, c + i, d):
                    return True
            # Swap: [a, a+i), [a+i, b), [c, d-i), [d-i, d)
            for i in range(1, b - a):
                if solve(a, a + i, d - i, d) and solve(a + i, b, c, d - i):
                    return True
            return False

        return solve(0, len(s1), 0, len(s2))

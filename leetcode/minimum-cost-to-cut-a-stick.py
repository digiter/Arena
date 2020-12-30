# 1547. Minimum Cost to Cut a Stick
# The difficulty is hard, but should be medium.
# O(len(cuts)^4)

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        @cache
        def dp(offset, length, left, right):
            if left == right:
                return 0

            ans = 10 ** 9
            for i in range(left, right):
                a = dp(offset, cuts[i] - offset, left, i)
                b = dp(cuts[i], length - (cuts[i] - offset), i + 1, right)
                ans = min(ans, length + a + b)
            return ans

        return dp(0, n, 0, len(cuts))

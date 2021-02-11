# 1458. Max Dot Product of Two Subsequences
# O(500 ** 2), 816 ms
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # Subsequences of nums1 and nums2 can be empty.
        @cache
        def solve(x, y):
            if x == -1 or y == -1:
                return 0
            ans = solve(x - 1, y - 1) + max(0, nums1[x] * nums2[y])
            ans = max(ans, solve(x, y - 1))
            ans = max(ans, solve(x - 1, y))
            return ans

        # Guarantees non-empty by enumerating a pair of nums1[x] and nums2[y].
        return max(
            nums1[x] * nums2[y] + solve(x - 1, y - 1)
            for x in range(len(nums1))
            for y in range(len(nums2))
        )

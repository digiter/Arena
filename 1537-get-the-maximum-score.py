# 1537. Get the Maximum Score

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        len1, len2 = len(nums1), len(nums2)
        x, y = 0, 0
        sum1, sum2 = 0, 0
        ans = 0

        while x < len1 and y < len2:
            if nums1[x] < nums2[y]:
                sum1 = (sum1 + nums1[x]) % MOD
                x += 1
            elif nums1[x] > nums2[y]:
                sum2 = (sum2 + nums2[y]) % MOD
                y += 1
            else:
                ans = (ans + max(sum1, sum2) + nums1[x]) % MOD
                sum1, sum2 = 0, 0
                x, y = x + 1, y + 1

        while x < len1:
            sum1 = sum1 + nums1[x]
            x += 1

        while y < len2:
            sum2 = sum2 + nums2[y]
            y += 1

        ans = (ans + max(sum1, sum2)) % MOD
        return ans

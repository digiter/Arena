# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# O(n)
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        # Number of changes to make [0, left) all zeros
        left = 0
        # Number of changes to make [right, n) all ones
        right = S.count('0')
        ans = left + right
        for i in range(n):
            if S[i] == '1':
                left += 1
            if S[i] == '0':
                right -= 1
            ans = min(ans, left + right)
        return ans

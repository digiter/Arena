# 1569. Number of Ways to Reorder Array to Get Same BST

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        def solve(a):
            if len(a) <= 1:
                return 1

            root = a[0]
            left = [x for x in a if x < root]
            right = [x for x in a if x > root]
            ans = solve(left)
            ans = ans * solve(right) % MOD
            ans = ans * math.comb(len(left) + len(right), len(left)) % MOD
            return ans

        return (solve(nums) - 1 + MOD) % MOD

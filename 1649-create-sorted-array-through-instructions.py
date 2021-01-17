# 1649. Create Sorted Array through Instructions
# See https://cp-algorithms.com/data_structures/fenwick.html

class FenwickTree:
    def __init__(self, n):
        self.t = [0] * (n + 1)

    def add(self, idx, x):
        while idx < len(self.t):
            self.t[idx] += x
            idx += idx & -idx

    def sum(self, idx):
        ans = 0
        while idx > 0:
            ans += self.t[idx]
            idx -= idx & -idx
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MAX_NUM = max(instructions)
        ft = FenwickTree(MAX_NUM)

        ans = 0
        for x in instructions:
            cost1 = ft.sum(x - 1)
            cost2 = ft.sum(MAX_NUM) - ft.sum(x)
            ans += min(cost1, cost2)
            ans %= 10 ** 9 + 7
            ft.add(x, 1)
        return ans

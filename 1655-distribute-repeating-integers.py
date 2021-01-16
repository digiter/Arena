# 1655. Distribute Repeating Integers
# Enumerates a subset of quantity to fill the ith freq.
# Dynamic programming, number of states: len(freq) * 2^len(quantity).
# Time complexity: O(3^len(quantity)), see https://cp-algorithms.com/algebra/all-submasks.html


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        supply = collections.Counter(nums)
        freq = list(supply.values())

        N = len(quantity)
        sumQuantity = [0] * (2 ** N)
        for subset in range(1, 2 ** N):
            sumQuantity[subset] = sum(
                quantity[i] if subset & (1 << i) else 0 for i in range(N)
            )

        @cache
        def solve(i, mask):
            if i == len(freq):
                return mask == 0
            subset = mask
            while subset > 0:
                if sumQuantity[subset] <= freq[i]:
                    if solve(i + 1, mask ^ subset):
                        return True
                subset = mask & (subset - 1)
            if solve(i + 1, mask ^ 0):
                return True
            return False

        return solve(0, 2 ** N - 1)

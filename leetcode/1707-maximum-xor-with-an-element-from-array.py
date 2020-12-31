# 1707. Maximum XOR With an Element From Array
# O(len(nums)*30 + len(queries)*30)

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # The length of 10**9 in binary format.
        LEN = 30

        # Contains prefixes with length i, 0 <= i < LEN.
        prefix = [set() for _ in range(LEN)]

        # Adds prefixes of num (in binary format).
        def add(num):
            for i in range(LEN):
                prefix[i].add(num >> i)

        def findMaxXor(num):
            want = ((1 << LEN) - 1) ^ num
            for i in range(LEN - 1, -1, -1):
                if (want >> i) not in prefix[i]:
                    want ^= 1 << i
            return want ^ num

        # Processes queries.
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda q: q[1])

        nums.sort()

        j = 0
        # The -2 is an invalid output which would indicate bugs if -2 occurs.
        ans = [-2] * len(queries)
        for (x, m, index) in queries:
            while j < len(nums) and nums[j] <= m:
                add(nums[j])
                j += 1
            if j == 0:
                # All elements in nums are larger than m.
                ans[index] = -1
            else:
                # Looks for max(nums[0:j] XOR x).
                ans[index] = findMaxXor(x)
        return ans

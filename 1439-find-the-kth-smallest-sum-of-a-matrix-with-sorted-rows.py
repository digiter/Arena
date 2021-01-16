# 1439. Find the Kth Smallest Sum of a Matrix With Sorted Rows
# Maintain the first 200 smallest sums and merge the rows one by one.
# O(40 * 200 * log(200))

from heapq import heappush, heappop
from collections import defaultdict


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])

        def merge(first200, row):
            h = []
            inHeap = defaultdict(bool)
            heappush(h, (first200[0] + row[0], 0, 0))
            inHeap[(0, 0)] = True
            next200 = []

            while h:
                s, f, r = heappop(h)
                next200.append(s)
                if f + 1 < len(first200) and (not inHeap[(f + 1, r)]):
                    heappush(h, (first200[f + 1] + row[r], f + 1, r))
                    inHeap[(f + 1, r)] = True
                if r + 1 < len(row) and (not inHeap[(f, r + 1)]):
                    heappush(h, (first200[f] + row[r + 1], f, r + 1))
                    inHeap[(f, r + 1)] = True
                if len(next200) == 200:
                    break
            return next200

        first200 = mat[0]
        for i in range(1, m):
            first200 = merge(first200, mat[i])
        return first200[k - 1]

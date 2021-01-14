# 1675. Minimize Deviation in Array
#
# Each number represents an interval: [lowerBound, upperBound].
# Makes all number to be even first, then slowly reduces the overall upperBound.

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        N = len(nums)
        evens = [x * 2 if x % 2 == 1 else x for x in nums]
        maxHeap = [-x for x in evens]
        heapq.heapify(maxHeap)
        lowerBound = min(evens)

        ans = 2 * 10 ** 9
        while len(maxHeap) == N:
            upperBound = -heapq.heappop(maxHeap)
            ans = min(ans, upperBound - lowerBound)
            if upperBound % 2 == 0:
                x = upperBound // 2
                heapq.heappush(maxHeap, -x)
                lowerBound = min(lowerBound, x)

        return ans

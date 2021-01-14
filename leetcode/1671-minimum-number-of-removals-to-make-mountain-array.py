# 1671. Minimum Number of Removals to Make Mountain Array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)

        def longestIncreasingSequence(arr):
            longestLength = [1]  # The LIS length at arr[0].
            tail = [0, arr[0]]  # The tail of the length 1 LIS is arr[0].
            for x in arr[1:]:
                pos = bisect.bisect_left(tail, x)
                if pos < len(tail):
                    tail[pos] = x
                else:
                    tail.append(x)
                longestLength.append(pos)
            return longestLength

        left = longestIncreasingSequence(nums)
        right = longestIncreasingSequence(list(reversed(nums)))

        ans = N
        for i in range(N):
            if left[i] >= 2 and right[N - 1 - i] >= 2:
                cost1 = i + 1 - left[i]
                cost2 = N - i - right[N - 1 - i]
                ans = min(ans, cost1 + cost2)
        return ans

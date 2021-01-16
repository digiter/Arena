# 1703. Minimum Adjacent Swaps for K Consecutive Ones
# O(len(nums))

class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if sum(nums) < k:
            return 0

        # Records the positions of 1s.
        pos = []
        for i in range(len(nums)):
            if nums[i] == 1:
                pos.append(i)

        # Calculates prefix sums.
        preSum = [0]
        for p in pos:
            preSum.append(preSum[-1] + p)

        # Considers a sliding window on pos, the cost is equal to
        # sum(pos[x2:y2]) - sum(pos[x1:y1]) - extra.
        #
        # Examples:
        # when k = 5, the cost is (pos[3]-pos[1]) + (pos[4]-pos[0]) - extra =
        # sum(pos[3:5]) - sum(pos[0:2]) - extra
        #
        # when k = 4, the cost is (pos[2]-pos[1]) + (pos[3]-pos[0]) - extra =
        # sum(pos[2:4]) - sum(pos[0:2]) - extra
        #
        half = k // 2
        if k % 2 == 1:
            x1, y1 = 0, half
            x2, y2 = half + 1, k
            extra = (1 + half) * half
        else:
            x1, y1 = 0, half
            x2, y2 = half, k
            extra = half * half

        ans = len(nums) * len(nums)
        while y2 <= len(pos):
            left = preSum[y1] - preSum[x1]
            right = preSum[y2] - preSum[x2]
            ans = min(ans, right - left - extra)
            x1, y1 = x1 + 1, y1 + 1
            x2, y2 = x2 + 1, y2 + 1
        return ans

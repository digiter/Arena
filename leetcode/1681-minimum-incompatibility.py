# 1681. Minimum Incompatibility
# O(C(N, SIZE-1)*N + C(N-SIZE, SIZE-1)*(N-SIZE) + C(N-SIZE*2, SIZE-1)*(N-SIZE*2) + ...)
# About O(10^5)

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        SIZE = N // k
        INF = nums[-1] * N + 5

        if SIZE == 1:
            return 0

        @cache
        def dp(fromNums):
            if len(fromNums) == SIZE:
                if len(set(fromNums)) == SIZE:
                    return fromNums[-1] - fromNums[0]
                else:
                    return INF

            ans = INF
            tail = fromNums[1:]
            candidates = set(tail)
            candidates.discard(fromNums[0])
            for chosen in combinations(sorted(candidates), SIZE - 1):
                toNums = []
                i = 0
                for x in tail:
                    if i < SIZE - 1 and x == chosen[i]:
                        i += 1
                        continue
                    toNums.append(x)
                ans = min(ans, dp(tuple(toNums)) + chosen[-1] - fromNums[0])
            return ans

        ans = dp(tuple(nums))
        return -1 if ans == INF else ans

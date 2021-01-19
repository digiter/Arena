# 1601. Maximum Number of Achievable Transfer Requests
# Time: 4572 ms

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        lenReq = len(requests)

        def isCircle(subset):
            inDegree = collections.Counter()
            outDegree = collections.Counter()
            for i in range(lenReq):
                if subset & (1 << i):
                    x, y = requests[i]
                    inDegree[y] += 1
                    outDegree[x] += 1
            if len(inDegree) != len(outDegree):
                return False
            for x in inDegree:
                if inDegree[x] != outDegree[x]:
                    return False
            return True

        # The number of elements when they form a circle.
        circleSize = [0] * (2 ** lenReq)
        for subset in range(1, len(circleSize)):
            if isCircle(subset):
                circleSize[subset] = bin(subset).count("1")

        @cache
        def solve(mask):
            subset = mask
            ans = 0
            while subset > 0:
                if circleSize[subset] > 0:
                    ans = max(ans, circleSize[subset] + solve(mask ^ subset))
                subset = mask & (subset - 1)
            return ans

        return solve(2 ** lenReq - 1)

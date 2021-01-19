# 1601. Maximum Number of Achievable Transfer Requests
# Straight forward simulation.
# Time: 2712 ms	

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        stay = sum(1 if x == y else 0 for x, y in requests)
        requests = [(x, y) for x, y in requests if x != y]
        lenReq = len(requests)

        ans = 0
        for subset in range(1, 2 ** lenReq):
            balance = collections.defaultdict(int)
            for i in range(lenReq):
                if subset & (1 << i):
                    x, y = requests[i]
                    balance[x] -= 1
                    balance[y] += 1
            if all(b == 0 for b in balance.values()):
                ans = max(ans, bin(subset).count("1"))

        return stay + ans

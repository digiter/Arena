# 1601. Maximum Number of Achievable Transfer Requests
# Time: O(2^len(requests)), 640 ms	

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        stay = sum(1 if x == y else 0 for x, y in requests)
        requests = [(x, y) for x, y in requests if x != y]
        lenReq = len(requests)

        balance = [0] * n

        def choose(i, usedCnt, zeroCnt):
            if i == lenReq:
                return usedCnt if zeroCnt == n else 0

            # Do not use request[i].
            ans1 = choose(i + 1, usedCnt, zeroCnt)

            # Or use request[i].
            x, y = requests[i]
            
            if balance[x] == 0:
                zeroCnt -= 1
            balance[x] -= 1
            if balance[x] == 0:
                zeroCnt += 1
            
            if balance[y] == 0:
                zeroCnt -= 1
            balance[y] += 1
            if balance[y] == 0:
                zeroCnt += 1
            
            ans2 = choose(i + 1, usedCnt + 1, zeroCnt)
            
            # Reverts changes.
            balance[x] += 1
            balance[y] -= 1

            return max(ans1, ans2)

        return stay + choose(0, 0, n)

# 1643. Kth Smallest Instructions

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        N = v + h
        ans = []
        for _ in range(N):
            if h > 0 and k <= math.comb(v + h - 1, v):
                ans.append("H")
                h -= 1
            else:
                ans.append("V")
                k -= comb(v + h - 1, v)
                v -= 1
        return "".join(ans)

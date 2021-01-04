# 1691. Maximum Height by Stacking Cuboids 
# O(N^3)

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()

        N = len(cuboids)
        enter = [False] * N
        exit = [False] * N
        ans = [a[2] for a in cuboids]

        def dfs(x):
            enter[x] = True
            a = cuboids[x]
            for y in range(N):
                if y == x:
                    continue
                b = cuboids[y]
                if a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]:
                    if not enter[y]:
                        dfs(y)
                    if exit[y]:
                        ans[x] = max(ans[x], ans[y] + a[2])
            exit[x] = True

        for x in range(N):
            if not enter[x]:
                dfs(x)

        return max(ans)

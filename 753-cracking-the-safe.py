# 753. Cracking the Safe
# O(n)

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(map(str, range(k)))

        ans = []
        seenEdge = set()

        def dfs(x):
            for last in map(str, range(k)):
                y = x[1:] + last
                if (x + last) not in seenEdge:
                    seenEdge.add(x + last)
                    dfs(y)
                    ans.append(last)

        dfs("0" * (n - 1))
        return "".join(ans) + "0" * (n - 1)

# 1697. Checking Existence of Edge Length Limited Paths
# Should be medium difficulty.

class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # Adds index to each query.
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda q: q[2])  # Sorts by limit.
        edgeList.sort(key=lambda e: e[2])  # Sorts by distance.

        # Creates disjoint sets for nodes.
        father = list(range(n))

        def findRoot(x):
            father[x] = x if x == father[x] else findRoot(father[x])
            return father[x]

        def merge(x, y):
            x = findRoot(x)
            y = findRoot(y)
            if randint(0, 1) == 0:
                father[x] = y
            else:
                father[y] = x

        # Processes queries.
        ans = [False] * len(queries)
        e = 0
        for (p, q, limit, index) in queries:
            while e < len(edgeList) and edgeList[e][2] < limit:
                merge(edgeList[e][0], edgeList[e][1])
                e += 1
            pRoot = findRoot(p)
            qRoot = findRoot(q)
            if pRoot == qRoot:
                ans[index] = True

        return ans

# https://leetcode.com/problems/escape-a-large-maze/
# Should be medium difficulty.

class Solution:
    def isEscapePossible(
        self, blocked: List[List[int]], source: List[int], target: List[int]
    ) -> bool:
        # Calculates the mapping
        def calcMapping(z):
            z.sort()
            mapz = {z[0]: 0}
            for i in range(1, len(z)):
                if z[i] == z[i - 1]:
                    continue
                elif z[i] == z[i - 1] + 1:
                    mapz[z[i]] = mapz[z[i - 1]] + 1
                else:
                    mapz[z[i]] = mapz[z[i - 1]] + 2
            return mapz

        mapx = calcMapping(
            [x for (x, y) in blocked] + [source[0], target[0], 0, 10 ** 6]
        )
        mapy = calcMapping(
            [y for (x, y) in blocked] + [source[1], target[1], 0, 10 ** 6]
        )

        # Rebuilt the board
        limitX = mapx[10 ** 6]
        limitY = mapy[10 ** 6]
        blocked = {(mapx[x], mapy[y]) for (x, y) in blocked}
        source = (mapx[source[0]], mapy[source[1]])
        target = (mapx[target[0]], mapy[target[1]])

        # Remove source and target from blocked
        blocked = {g for g in blocked if g != source and g != target}

        # DFS
        visited = defaultdict(bool)

        def dfs(x, y):
            if 0 <= x and x < limitX and 0 <= y and y < limitY:
                if visited[(x, y)]:
                    return
                if (x, y) in blocked:
                    return
                visited[(x, y)] = True
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)

        dfs(source[0], source[1])
        return visited[target]

# 803. Bricks Falling When Hit
# Applies the hit backwards and merges connected components on the go.
# O(M*N + M*N + M*N*4*log(M*N) + len(hits)*4*log(M*N))

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        BRICK, SPACE = 1, 0
        CELLING = (-1, -1)
        M = len(grid)
        N = len(grid[0])

        # Initializes a disjoint set for each brick.
        father = dict()
        size = dict()
        for x in range(M):
            for y in range(N):
                if grid[x][y] == BRICK:
                    t = (x, y)
                    father[t] = t
                    size[t] = 1
        father[CELLING] = CELLING
        size[CELLING] = 1

        # Calculates the final status.
        final = copy.deepcopy(grid)
        for (x, y) in hits:
            final[x][y] = SPACE

        # Connects the disjoint sets on the final status, includes the celling.
        def findRoot(t):
            root = t if t == father[t] else findRoot(father[t])
            father[t] = root
            return root

        def merge(t1, t2):
            t1 = findRoot(t1)
            t2 = findRoot(t2)
            if t1 == t2:
                return
            if random.randint(1, 2) == 1:
                father[t2] = t1
                size[t1] += size[t2]
            else:
                father[t1] = t2
                size[t2] += size[t1]

        for x in range(M):
            for y in range(N):
                if final[x][y] == BRICK:
                    for (nx, ny) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                        if nx == -1:
                            merge((x, y), CELLING)
                            continue
                        if 0 <= nx and nx < M and 0 <= ny and ny < N:
                            if final[nx][ny] == BRICK:
                                merge((x, y), (nx, ny))

        # Adds bricks backwards.
        ans = []
        for (x, y) in reversed(hits):
            if not (grid[x][y] == BRICK):
                ans.append(0)
                continue

            before = size[findRoot(CELLING)]

            # Merges the brick with neighbours.
            final[x][y] = BRICK
            for (nx, ny) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if nx == -1:
                    merge((x, y), CELLING)
                    continue
                if 0 <= nx and nx < M and 0 <= ny and ny < N:
                    if final[nx][ny] == BRICK:
                        merge((x, y), (nx, ny))

            after = size[findRoot(CELLING)]
            if after == before:
                ans.append(0)
            else:
                ans.append(after - before - 1)

        return reversed(ans)

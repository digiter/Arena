# 1728. Cat and Mouse II

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rowCnt = len(grid)
        colCnt = len(grid[0])

        index = lambda x, y: x * colCnt + y

        def buildGraph(jumpCnt):
            g = [list() for _ in range(rowCnt * colCnt)]
            for x in range(rowCnt):
                for y in range(colCnt):
                    if grid[x][y] != "#":
                        node = g[index(x, y)]
                        node.append(index(x, y))
                        for d in range(1, jumpCnt + 1):
                            if not (0 <= x - d and grid[x - d][y] != "#"):
                                break
                            node.append(index(x - d, y))
                        for d in range(1, jumpCnt + 1):
                            if not (x + d < rowCnt and grid[x + d][y] != "#"):
                                break
                            node.append(index(x + d, y))
                        for d in range(1, jumpCnt + 1):
                            if not (0 <= y - d and grid[x][y - d] != "#"):
                                break
                            node.append(index(x, y - d))
                        for d in range(1, jumpCnt + 1):
                            if not (y + d < colCnt and grid[x][y + d] != "#"):
                                break
                            node.append(index(x, y + d))
            return g

        mouseGraph = buildGraph(mouseJump)
        catGraph = buildGraph(catJump)

        food, mouse, cat = None, None, None
        for x in range(rowCnt):
            for y in range(colCnt):
                if grid[x][y] == "F":
                    food = index(x, y)
                elif grid[x][y] == "M":
                    mouse = index(x, y)
                elif grid[x][y] == "C":
                    cat = index(x, y)

        MOUSE_WIN, CAT_WIN = 1, 2

        @cache
        def play(step, mouse, cat):
            if step == 1000:
                return CAT_WIN
            if step == 2 * rowCnt * colCnt:
                return CAT_WIN
            if mouse == cat:
                return CAT_WIN
            if cat == food:
                return CAT_WIN
            if mouse == food:
                return MOUSE_WIN

            if step % 2 == 0:
                for nextMouse in mouseGraph[mouse]:
                    if play(step + 1, nextMouse, cat) == MOUSE_WIN:
                        return MOUSE_WIN
                return CAT_WIN
            else:
                for nextCat in catGraph[cat]:
                    if play(step + 1, mouse, nextCat) == CAT_WIN:
                        return CAT_WIN
                return MOUSE_WIN

        return play(0, mouse, cat) == MOUSE_WIN

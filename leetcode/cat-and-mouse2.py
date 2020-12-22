# https://leetcode.com/problems/cat-and-mouse/
# O(2 * N^3)

from typing import List
from collections import defaultdict
from queue import SimpleQueue

MOUSE, CAT, DRAW = 1, 2, 0


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        state = dict()  # mouse, cat, turn -> result
        que = SimpleQueue()

        def enqueue(mouse, cat, turn, result):
            s = (mouse, cat, turn)
            if not (s in state):
                state[s] = result
                que.put(s)

        n = len(graph)
        for cat in range(1, n):  # The cat can not enter the hole.
            enqueue(0, cat, MOUSE, MOUSE)
            enqueue(0, cat, CAT, MOUSE)
            enqueue(cat, cat, MOUSE, CAT)
            enqueue(cat, cat, CAT, CAT)

        # mouse, cat, turn -> number of neighbours
        neighbourCount = dict()
        # mouse, cat, turn -> number of updates
        updateCount = defaultdict(int)
        # mouse, cat, turn -> if the current player can draw
        canDraw = defaultdict(bool)
        for mouse in range(n):
            for cat in range(1, n):
                neighbourCount[(mouse, cat, MOUSE)] = len(graph[mouse])
                neighbourCount[(mouse, cat,
                                CAT)] = len(graph[cat]) - (0 in graph[cat])

        def update(mouse, cat, turn, result):
            s = (mouse, cat, turn)
            updateCount[s] += 1
            if result == DRAW:
                canDraw[s] = True

            bestResult, worstResult = turn, MOUSE + CAT - turn
            # Quick win
            if result == bestResult:
                enqueue(mouse, cat, turn, bestResult)
                return
            # Updated from all neighbours
            if updateCount[s] == neighbourCount[s]:
                enqueue(mouse, cat, turn, DRAW if canDraw[s] else worstResult)

        while not que.empty():
            mouse, cat, turn = que.get()
            result = state[(mouse, cat, turn)]

            prevTurn = MOUSE + CAT - turn
            if prevTurn == MOUSE:
                for prevMouse in graph[mouse]:
                    update(prevMouse, cat, prevTurn, result)
            else:
                for prevCat in graph[cat]:
                    if prevCat != 0:
                        update(mouse, prevCat, prevTurn, result)

        end = (1, 2, MOUSE)
        if end in state:
            return state[end]
        return DRAW


if __name__ == "__main__":
    grah = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
    print(Solution().catMouseGame(grah))

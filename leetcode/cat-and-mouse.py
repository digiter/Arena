from typing import List

MOUSE, CAT, DRAW = 1, 2, 0


# O(2 * n^3) states and O(n) ways of transition -> O(n^4)
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        memo = dict()

        def dfs(mouse: int, cat: int, level: int):
            if level == len(graph) * 2:
                return DRAW  # Exhausted all states
            current = (mouse, cat, level)
            if current in memo:
                return memo[current]

            if mouse == 0:
                memo[current] = MOUSE
                return memo[current]
            if mouse == cat:
                memo[current] = CAT
                return memo[current]

            mouse_turn = (level % 2) == 0
            childResult = CAT if mouse_turn else MOUSE  # Worst case scenario
            for child in graph[mouse if mouse_turn else cat]:
                if not mouse_turn and child == 0:
                    continue  # The cat can not enter the hole
                result = dfs(child, cat, level + 1) if mouse_turn else dfs(
                    mouse, child, level + 1)
                if result == (MOUSE if mouse_turn else CAT):
                    childResult = result  # Best case scenario
                    break
                elif result == DRAW:
                    childResult = DRAW  # Better than worst case

            memo[current] = childResult
            return memo[current]

        return dfs(1, 2, 0)

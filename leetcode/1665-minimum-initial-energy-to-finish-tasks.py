# 1665. Minimum Initial Energy to Finish Tasks
# Proof of greedy:
#   Consider any two tasks: (a1, m1) and (a2, m2).
#   Assume m1-a1 >= m2-a2, then m1+a2 >= m2+a1
#   If we do task1 first, then the initial energy = a1 + m2
#   If we do task2 first, then the initial energy = a2 + m1
#   Therefore it's optimal to do task1 first.

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Sorts by minimum - actual in decreasing order.
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)

        initial, current = tasks[0][1], tasks[0][1] - tasks[0][0]
        for actual, minimum in tasks[1:]:
            if current < minimum:
                delta = minimum - current
                current += delta
                initial += delta
            current -= actual
        return initial

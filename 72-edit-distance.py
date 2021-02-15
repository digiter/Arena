# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(x, y):
            if x == -1:
                return y + 1
            if y == -1:
                return x + 1

            if word1[x] == word2[y]:
                return solve(x - 1, y - 1)
            # We only need to apply operations to word2, there are 3 cases:
            return 1 + min(
                solve(x - 1, y),  # Inserts word1[x] after word2[y].
                solve(x, y - 1),  # Deletes word2[y].
                solve(x - 1, y - 1),  # Replaces word2[y] with word1[x].
            )

        return solve(len(word1) - 1, len(word2) - 1)

# 329. Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        order = []
        for x in range(M):
            for y in range(N):
                order.append((x, y))
        order.sort(key=lambda o: matrix[o[0]][o[1]])  # Sorts by element.

        dp = copy.deepcopy(matrix)
        for x in range(M):
            for y in range(N):
                dp[x][y] = 1

        for (x, y) in order:
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if not (0 <= nx and nx < M and 0 <= ny and ny < N):
                    continue
                if not (matrix[nx][ny] > matrix[x][y]):
                    continue
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)

        ans = max(max(row) for row in dp)
        return ans

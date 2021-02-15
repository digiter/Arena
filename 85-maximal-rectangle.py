# 85. Maximal Rectangle
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        Elem = collections.namedtuple("Elem", ["position", "height"])
        if (not matrix) or (not matrix[0]):
            return 0

        heights = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            n = len(row)
            heights = [0 if row[i] == "0" else heights[i] + 1 for i in range(n)]

            stack = []
            left = [0] * n
            for x in range(n):
                while stack and stack[-1].height >= heights[x]:
                    stack.pop()
                left[x] = stack[-1].position if stack else -1
                stack.append(Elem(position=x, height=heights[x]))

            stack = []
            right = [0] * n
            for x in range(n - 1, -1, -1):
                while stack and stack[-1].height >= heights[x]:
                    stack.pop()
                right[x] = stack[-1].position if stack else n
                stack.append(Elem(position=x, height=heights[x]))

            for x in range(n):
                width = right[x] - (left[x] + 1)
                ans = max(ans, heights[x] * width)

        return ans

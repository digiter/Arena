# 42. Trapping Rain Water
# Whenever a bar occurs, the bars that are lower than it on the left are no longer useful.
# Hence the bar height to consider is monotonically decreasing.
class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        water = 0
        for pos, height in enumerate(heights):
            low = 0
            while stack and height >= stack[-1][1]:
                leftPos, leftHeight = stack[-1]
                stack.pop()

                width = pos - leftPos - 1
                water += width * (leftHeight - low)

                low = leftHeight

            if stack:
                leftPos, leftHeight = stack[-1]
                width = pos - leftPos - 1
                water += width * (height - low)

            stack.append((pos, height))

        return water

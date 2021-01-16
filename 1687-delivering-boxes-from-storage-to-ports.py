# 1687. Delivering Boxes from Storage to Ports
# Inspired from https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/discuss/969560/Python-O(n).-DP-%2B-Monotonic-Queue-(Sliding-Window)-with-Full-Explanation


class Solution:
    def boxDelivering(
        self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        N = len(boxes)
        ports = [b[0] for b in boxes]
        weights = [b[1] for b in boxes]

        # Ignores limitations and ships boxes [0, i] together.
        together = [0] * N
        together[0] = 2
        for y in range(1, N):
            together[y] = together[y - 1] + (0 if ports[y] == ports[y - 1] else 1)

        # The extra cost when splitting between y and y+1, so that we will
        # travel from ports[y] to the storage then to ports[y+1].
        splitCost = lambda y: 2 - (0 if y + 1 < N and ports[y] == ports[y + 1] else 1)

        prefixWeight = [0] * N
        prefixWeight[0] = weights[0]
        for y in range(1, N):
            prefixWeight[y] = prefixWeight[y - 1] + weights[y]
        # Adds a dummy value to make prefixWeight[-1] useful.
        prefixWeight.append(0)

        # Splits the last portion to satisfy the constraints, which adds extra costs.
        extra = [0] * (N + 1)
        heap = []
        heappush(heap, (extra[-1], -1))
        for y in range(0, N):
            while True:
                prevCost, prevSplit = heap[0]
                if (y - prevSplit > maxBoxes) or (
                    prefixWeight[y] - prefixWeight[prevSplit] > maxWeight
                ):
                    heappop(heap)
                else:
                    break
            extra[y] = prevCost
            heappush(heap, (extra[y] + splitCost(y), y))

        return together[N - 1] + extra[N - 1]

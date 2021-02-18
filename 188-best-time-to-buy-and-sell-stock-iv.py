# 188. Best Time to Buy and Sell Stock IV
# The split-or-add approach.
# O(nlogn), 40 ms.
#
# Critical test case:
# Case #1: 1 [1, 10, 8, 9, 6, 12]
# Case #2: 3 [1, 10, 8, 9, 6, 12]
# Case #3: 1 [1, 5, 2, 4, 3, 6]


class Trade:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def profit(self):
        return self.high - self.low


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Saves all the profitable dayTrades.
        dayTrades = []
        for x in range(1, len(prices)):
            if prices[x - 1] < prices[x]:
                dayTrades.append(Trade(prices[x - 1], prices[x]))

        def merge(x, y):
            return Trade(x.low, y.high)

        # Overall strategy: tries to merge as many consecutive dayTrades as possible.
        # A mergedTrade has the characteristic of being better than any of its containing dayTrades.
        mergedTrades = []
        # A splitGain records how much profit will be gained when spliting two consecutive dayTrades inside a mergedTrade.
        splitGains = []
        stack = []
        for t in dayTrades:
            stack.append(t)

            # While merging stack[-2] is not better than stack[-1].
            # (Below condition is equivalent to `stack[-2].low >= stack[-1].low`)
            while (
                len(stack) >= 2
                and merge(stack[-2], stack[-1]).profit() <= stack[-1].profit()
            ):
                # Why we can safely remove stack[-1] without worrying breaking consecutiveness?
                # If later stack[before] is merged with t, the splitGain is always >= stack[-1].
                # So that if we need to add stack[-1] to the final result, the splitting between stack[before] and t must already happened.
                # See test case #2 for an example.
                mergedTrades.append(stack[-2])
                stack[-2] = stack[-1]
                stack.pop()

            # While we should merge stack[-2] and stack[-1].
            # See test case #3 for an example.
            while len(stack) >= 2:
                merged = merge(stack[-2], stack[-1])
                # (Below condition is equivalent to `stack[-2].low < stack[-1].low and stack[-2].high < stack[-1].high)
                if (
                    merged.profit() > stack[-2].profit()
                    and merged.profit() > stack[-1].profit()
                ):
                    splitGains.append(
                        stack[-2].profit() + stack[-1].profit() - merged.profit()
                    )
                    stack[-2] = merged
                    stack.pop()
                else:
                    break
        while stack:
            mergedTrades.append(stack.pop())

        # Greedily chooses the largest k gains.
        # There are two type of gains:
        #   - add a mergedTrade (which is always safe, see test case #2 for an example)
        #   - split two merged trades
        gains = [t.profit() for t in mergedTrades] + splitGains
        gains.sort(reverse=True)
        return sum(gains[:k])

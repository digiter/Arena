# 354. Russian Doll Envelopes

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
            
        # Sorts by width increasing,
        # and when two widths are equal, sorts by height decreasing.
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        # The tail height of the longest increasing sequence at length x.
        tail = [-1, envelopes[0][1]]
        for (_, h) in envelopes[1:]:
            pos = bisect.bisect_left(tail, h)
            if pos == len(tail):
                tail.append(h)
            else:
                tail[pos] = h
        return len(tail) - 1

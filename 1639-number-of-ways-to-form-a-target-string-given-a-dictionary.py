# 1639. Number of Ways to Form a Target String Given a Dictionary

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        wordLen = len(words[0])
        targetLen = len(target)

        freq = [collections.Counter() for _ in range(wordLen)]
        for word in words:
            for wid in range(wordLen):
                freq[wid][word[wid]] += 1

        @cache
        def solve(wid, tid):
            if not (wordLen - wid >= targetLen - tid):
                return 0
            if tid == targetLen:
                return 1 if wid <= wordLen else 0

            # First choice: matches word[wid] with target[tid].
            ans1 = 0
            if freq[wid][target[tid]] > 0:
                ans1 = freq[wid][target[tid]] * solve(wid + 1, tid + 1)
            # Second choice: skips word[wid]
            ans2 = solve(wid + 1, tid)
            return (ans1 + ans2) % (10 ** 9 + 7)

        return solve(0, 0)

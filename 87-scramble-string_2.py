# 87. Scramble String
# O(30^5), 36ms
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def solve(s1, s2):
            if len(s1) == 0:
                return True
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            
            # Same order.
            for i in range(1, len(s1)):
                if solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:]):
                    return True
            # Swap.
            for i in range(1, len(s1)):
                if solve(s1[:i], s2[-i:]) and solve(s1[i:], s2[:-i]):
                    return True
            return False
        
        return solve(s1, s2)

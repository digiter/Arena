# 1510. Stone Game IV
# Roughtly O(n * sqrt(n))

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @cache
        def solve(pile):
            if pile == 0:
                return False
            for t in range(1, pile+1):
                if t * t <= pile:
                    currentPlayerWins = solve(pile - t * t)
                    if not currentPlayerWins:
                        return True
                else:
                    break
            return False
        
        return solve(n)

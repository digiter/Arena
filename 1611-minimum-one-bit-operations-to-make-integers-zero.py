# 1611. Minimum One Bit Operations to Make Integers Zero
#
# The whole process is reversable as the two operations are reversable.
#
# Consider making the highest bit from zero, for example 2**2:
# 000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100
# The second part is removing the 2nd highest bit, i.e. 2**1 from 110.
#
# So after adding the cost of 2^x, if the next bit is 1, it needs to substract
# the cost of 2^(x-1). The current number will be 11000...
#
# Repeat this process for the remaining bits.

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # The cost of making 2^i from zero.
        powerCost = [1]
        for i in range(1, 32 + 1):
            powerCost.append(powerCost[i - 1] * 2 + 1)

        cost = 0
        sign = +1
        binN = bin(n)
        for i in range(len(binN)):
            if binN[i] == "1":
                cost += sign * powerCost[len(binN) - 1 - i]
                sign *= -1
        return cost

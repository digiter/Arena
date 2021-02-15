# 32. Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        before = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop() # Matches a '('.
                    if stack:
                        ans = max(ans, i-stack[-1])
                    else:
                        ans = max(ans, i-before)
                else:
                    before = i # Discards previous '('s.
        return ans

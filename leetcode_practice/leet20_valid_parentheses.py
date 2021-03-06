"""
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if
the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

solution = Solution()
print(solution.isValid("{([])}"))
print(solution.isValid("[{]}"))
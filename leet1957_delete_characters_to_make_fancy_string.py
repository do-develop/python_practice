class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 1 and c == stack[-1] == stack[-2]:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

class Solution:
    def isValid(self, s: str) -> bool:
        # keep a track of characters in stack
        # when meet c, pop a and b at the end of stack
        # otherwise false
        stack = []
        for c in s:
            if c == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(c)
        return not stack # if empty True

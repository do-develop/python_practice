class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack= []
        splitted = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) != 0:
                    stack.pop()
                else:
                    splitted[i] = ''
        
        for i in stack:
            splitted[i] = ''
        return ''.join(splitted)

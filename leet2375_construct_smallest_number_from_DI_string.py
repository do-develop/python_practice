class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stack = [], []
        for i, c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)

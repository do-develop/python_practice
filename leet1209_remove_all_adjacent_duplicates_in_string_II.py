class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#', 0]] # stack with a dummy data
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        res = ''
        for c, k in stack:
            res += c * k
        return ''.join(res)

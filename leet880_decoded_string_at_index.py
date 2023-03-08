class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack, cur_len = [], 0
        for c in s:
            cur_len = cur_len + 1 if c.isalpha() else cur_len * int(c)
            stack += c
            while cur_len >= k:
                while stack[-1].isdigit():
                    cur_len //= int(stack.pop())
                k = k % cur_len
                if not k:
                    return stack[-1]
                cur_len -= 1
                stack.pop()

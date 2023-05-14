class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # store last occurence of each character
        last_idx = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and i < last_idx[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)

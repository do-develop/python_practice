"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        stack = stack[:len(stack) - k]
        result = "".join(stack)

        # handle leading zero cases
        return str(int(result)) if result else "0"


num = "1432219"
k = 3
print(Solution().removeKdigits(num, k))
#Output: "1219"

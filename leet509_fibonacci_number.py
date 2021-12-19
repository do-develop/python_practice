"""
# Recursive version
class Solution:
    def fib(self, number: int) -> int:
        if number <= 1:
            return number
        return self.fib(number-1) + self.fib(number-2)

# Dinamic Programming
import collections

class Solution:
    dp = collections.defaultdict(int)
    def fibonacci(self, number: int) -> int:
        self.dp[1] = 1

        for i in range(2, number+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[number]
"""

# Dynamic programming with two variables only

class Solution:
    def fibonacci(self, number: int) -> int:
        x, y = 0, 1
        for i in range(0, number):
            x, y = y, x + y
        return x


# Test
print(Solution().fibonacci(8))
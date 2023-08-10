class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 2]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        ans = 0
        i = len(fib) - 1
        while k > 0:
            ans += k // fib[i]
            k %= fib[i]
            i -= 1
        return ans

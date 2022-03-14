"""
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You
want to arrange the sticks such that exactly k sticks are visible from the left.
A stick is visible from the left if there are no longer sticks to the left of
it. For example, if the sticks are arranged [1,3,2,5,4], then the sticks with
lengths 1, 3, and 5 are visible from the left. Given n and k, return the number
of such arrangements. Since the answer may be large, return it modulo 10**9 + 7.
"""

class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {}

        def dfs(N, K):
            if N == K:
                return 1
            if N == 0 or K == 0:
                return 0
            if (N, K) in dp:
                return dp[(N, K)]

            dp[(N, K)] = (dfs(N - 1, K - 1) +
                          (N - 1) * dfs(N - 1, K))
            return dp[(N, K)]
        
        return dfs(n, k) % (10 **9 + 7)
            





# TEST
n = 20
k = 11
print(Solution().rearrangeSticks(n, k))
# expected output: 647427950
"""
Explanation: There are 647427950 (mod 10^9 + 7) ways to rearrange the sticks
such that exactly 11 sticks are visible.
"""

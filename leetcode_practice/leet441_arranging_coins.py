"""
You have n coins and you want to build a staircase with these coins. The
staircase consists of k rows where the ith row has exactly i coins. The last
row of the staircase may be incomplete. Given the integer n, return the number
of complete rows of the staircase you will build.
"""



class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        result = 0
        while l <= r:
            mid = (l + r) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                result = max(mid, result)
        return result
            


n = 8
print(Solution().arrangeCoins(n))
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.

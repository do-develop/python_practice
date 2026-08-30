from typing import List

class Solution:
    def kth_root(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        r = int(round(n ** (1 / k)))
        while r ** k > n:
            r -= 1
        while (r + 1) ** k <= n:
            r += 1
        return r

    def minDifference(self, n: int, k: int) -> List[int]:
        if k == 1:
            return [n]

        best, ans = float('inf'), []

        upper = self.kth_root(n, k)
        for cand in range(1, upper + 1):
            if n % cand != 0:
                continue

            divs = self.minDifference(n // cand, k - 1)
            divs = divs + [cand]
            mini, maxi = min(divs), max(divs)

            if maxi - mini < best:
                best, ans = maxi - mini, divs

        return ans
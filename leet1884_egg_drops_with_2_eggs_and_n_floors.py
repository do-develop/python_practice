class Solution:
    def twoEggDrop(self, n: int) -> int:
        # the intuition is increasing the interval incrementally
        # instead of binary search
        interval = 1

        while n > 0:
            n -= interval
            interval += 1
        return interval - 1

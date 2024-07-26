class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # Intuition: Fix the number of pencils purchased and calculate 
        #            the number of ways to buy pens.

        count = 0

        while total >= 0:
            count += (total // cost2) + 1 # +1 for the case that you don't buy anything
            total -= cost1
        return count

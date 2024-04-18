class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # All shortest paths have the same cost
        # From the view of row index, the best path will be go directly from start x to home x
        # From the view of col index, the best path will be go directly from start y to home y
        cost = 0
        [i, j], [x, y] = startPos, homePos

        while i != x:
            i = i + 1 if i < x else i - 1
            cost += rowCosts[i]

        while j != y:
            j = j + 1 if j < y else j - 1
            cost += colCosts[j]

        return cost

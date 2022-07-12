"""
There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two adjacent
houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3
cost matrix. For example, costs[0][0] is the cost of painting house 0 with color
red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.
"""
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0
        for r, b, g in costs:
            red, blue, green = r + min(blue, green), b + min(red, green), g + min(red, blue)

        return min(red, blue, green)
            
        


# TEST
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(Solution().minCost(costs))
"""
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2
            into blue. Minimum cost: 2 + 5 + 3 = 10.
"""

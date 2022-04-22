"""
You are given an integer array cost where cost[i] is the cost of ith step on a
staircase. Once you pay the cost, you can either climb one or two steps. You
can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
"""
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])
        



# TEST
cost = [10,15,20]
print(Solution().minCostClimbingStairs(cost))
"""
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
"""

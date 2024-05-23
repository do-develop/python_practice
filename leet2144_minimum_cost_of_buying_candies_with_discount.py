class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        cost.sort(reverse=True)

        for i in range(len(cost)):
            if i == 0 or (i + 1) % 3 != 0:
                total += cost[i]
        return total

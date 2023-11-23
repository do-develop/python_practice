class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(idx, cost):
            if idx == len(toppingCosts) or cost > target:
                return cost
            
            new_topping = toppingCosts[idx]
            ans = (dp(idx + 1, cost), dp(idx + 1, cost + new_topping), dp(idx + 1, cost + 2 * new_topping))
            return min(ans, key=lambda x: (abs(x - target), x))
        
        # get answer for each base
        ans = (dp(0, cost) for cost in baseCosts)
        return min(ans, key=lambda x: (abs(x - target), x))

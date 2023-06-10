class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}
        def dp(dice, target):
            # base case: we can make target = 0 with 0 dice
            if dice == 0:
                return 1 if target == 0 else 0
            if (dice, target) in memo:
                return memo[(dice, target)]
            rolls = 0
            for i in range(max(0, target - k), target):
                rolls += dp(dice - 1, i)
            memo[(dice, target)] = rolls
            return rolls
        return dp(n, target) % (10**9 + 7)

            

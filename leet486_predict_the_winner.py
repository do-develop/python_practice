class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp approach with memoization
        memo = {}
        def max_score(i, j):
            # base cases
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j:
                return 0
            # player2 will play optimally thus player1 will achieve minimum score
            scenario1 = nums[i] + min(max_score(i+2, j), max_score(i+1, j-1))
            scenario2 = nums[j] + min(max_score(i+1, j-1), max_score(i, j-2))
            score = max(scenario1, scenario2) # among two different scenario which one is better?
            memo[(i, j)] = score
            return score
        
        player1 = max_score(0, len(nums)-1)
        return player1 >= (sum(nums) - player1) # final check: player1 >= player2

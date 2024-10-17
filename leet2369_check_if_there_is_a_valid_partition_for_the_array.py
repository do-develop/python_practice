class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = {} # remember the result of subproblems
        N = len(nums)

        def solve(idx):
            # base case
            if idx == N:
                return True

            validity = False
            if idx in memo: # subproblem already computed?
                return memo[idx]
            
            if idx < N - 1 and nums[idx] == nums[idx + 1]:
                validity = validity or solve(idx + 2)
            if idx < N - 2 and nums[idx] == nums[idx + 1] == nums[idx + 2]:
                validity = validity or solve(idx + 3)
            if idx < N - 2 and nums[idx] + 1 == nums[idx + 1] and nums[idx + 1] + 1 == nums[idx + 2]:
                validity = validity or solve(idx + 3)
            
            # store the result
            memo[idx] = validity
            return validity
        
        return solve(0)

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N, numCounter = len(nums), Counter(nums)
        score = gcd(*nums) * lcm(*nums)

        if N > 1:
            for i in range(N):
                if numCounter[nums[i]] > 1:
                    continue
                
                arr = nums[:i] + nums[i+1:]
                score = max(score, gcd(*arr) * lcm(*arr))
        
        return score

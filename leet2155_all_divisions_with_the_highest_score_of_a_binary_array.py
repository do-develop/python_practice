class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        lscore = 0
        rscore = sum(nums)

        divsum = [lscore + rscore]

        for i in range(len(nums)):
            if nums[i] == 0:
                lscore += 1
            if nums[i] == 1:
                rscore -= 1
            divsum.append(lscore + rscore)
        
        maxscore = max(divsum)

        return [idx for idx, val in enumerate(divsum) if val == maxscore]

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        ans = {0}

        for reward in rewardValues:
            newRewards = set()
            for x in ans:
                if reward > x :
                    newRewards.add(x + reward)
            ans.update(newRewards)
        return max(ans)

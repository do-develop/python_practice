class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score = list(zip(ages, scores))
        age_score.sort(key=lambda x: (x[0], x[1]))
        dp = [0] * len(scores)
        best = 0
        
        for i, (age, sc) in enumerate(age_score):
            dp[i] = sc
            for j in range(i):
                if age_score[j][1] <= sc:
                    dp[i] = max(dp[j] + sc, dp[i])
            if dp[i] > best:
                best = dp[i]
        return best

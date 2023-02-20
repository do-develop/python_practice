class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = zip(difficulty, profit)
        jobs = sorted(jobs, key=lambda x:x[0]) # sort by difficulty
        max_profit = idx = best = 0

        for skill in sorted(worker):
            while idx < len(jobs) and skill >= jobs[idx][0]:
                best = max(best, jobs[idx][1])
                idx += 1
            max_profit += best
        return max_profit

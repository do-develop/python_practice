class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        N = len(b)
        dpPrev = [float('-inf')] * N 
        dpCurr = [float('-inf')] * N

        for i in range(N):
            dpPrev[i] = a[0] * b[i]

        for k in range(1, 4):
            maxSoFar = float('-inf')
            for i in range(k, N):
                maxSoFar = max(maxSoFar, dpPrev[i - 1])
                dpCurr[i] = maxSoFar + a[k] * b[i]

            dpPrev = dpCurr.copy()
        return max(dpPrev[3:])

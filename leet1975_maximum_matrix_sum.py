class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_total = neg = 0
        mini = math.inf
        for row in matrix:
            for num in row:
                abs_total += abs(num)
                if num < 0:
                    neg += 1
                mini = min(mini, abs(num))
        return abs_total if neg % 2 == 0 else abs_total - 2 * mini

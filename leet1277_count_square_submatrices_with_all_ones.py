class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        result = 0
        for r in range(0, len(matrix)):
            for c in range(0, len(matrix[0])):
                if (matrix[r][c] > 0 and r > 0 and c > 0):
                    matrix[r][c] = min(matrix[r - 1][c], matrix[r][c - 1], matrix[r-1][c-1]) + 1        
                result += matrix[r][c]
        return result

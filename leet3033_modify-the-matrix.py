class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        maxCol = [-1] * cols

        for c, r in product(range(cols), range(rows)):
            maxCol[c] = max(maxCol[c], matrix[r][c])

        for r, c in product(range(rows), range(cols)):
            if matrix[r][c] == -1:
                matrix[r][c] = maxCol[c]

        return matrix
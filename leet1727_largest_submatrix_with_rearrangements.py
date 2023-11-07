class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prev_row = [0] * cols
        area = 0

        for r in range(rows):
            curr_row = matrix[r][:]
            for c in range(cols):
                if curr_row[c] != 0:
                    curr_row[c] += prev_row[c]
                
            sorted_row = sorted(curr_row, reverse=True)
            for i in range(cols):
                area = max(area, sorted_row[i] * (i + 1))
            prev_row = curr_row
                
        return area

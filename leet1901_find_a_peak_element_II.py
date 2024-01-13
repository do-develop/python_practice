class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        # binary search
        start_col = 0
        end_col = len(mat[0]) - 1

        while start_col <= end_col:
            max_row = 0
            mid_col = (end_col + start_col) // 2

            for row in range(len(mat)):
                max_row = row if (mat[row][mid_col] >= mat[max_row][mid_col]) else max_row
            
            left_is_big = mid_col - 1 >= start_col and mat[max_row][mid_col -1] > mat[max_row][mid_col]
            right_is_big = mid_col + 1 <= end_col and mat[max_row][mid_col + 1] > mat[max_row][mid_col]

            # fount the peak element?
            if (not left_is_big) and (not right_is_big):
                return [max_row, mid_col]
            elif right_is_big:
                start_col = mid_col + 1
            else:
                end_col = mid_col - 1
        return []

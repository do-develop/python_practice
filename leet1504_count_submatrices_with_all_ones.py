class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # DP approach
        ROW, COL = len(mat), len(mat[0])
        total = 0
        for up_row in range(ROW):
            for down_row in range(up_row, ROW):
                rect_at = [0 for _ in range(COL)]
                for c in range(COL):
                    rect_at[c] = rect_at[c-1] + 1 if all(mat[row][c] == 1 for row in range(up_row, down_row + 1)) else 0
                total += sum(rect_at)
        return total

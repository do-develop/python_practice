class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        ROW, COL = len(mat), len(mat[0])
        result, intermediate = [], []

        # count of diagonal = ROW + COL - 1
        for d in range(ROW + COL - 1):
            intermediate.clear()
            r, c = 0 if d < COL else d - COL + 1, d if d < COL else COL - 1

            while r < ROW and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result

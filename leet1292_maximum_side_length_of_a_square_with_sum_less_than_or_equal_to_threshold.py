class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # part 1: get prefix sum
        ROWS, COLS = len(mat), len(mat[0])
        prefix = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        # top rect + left rect - double counted rect
        for r in range(ROWS):
            for c in range(COLS):
                prefix[r + 1][c + 1] = prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c] + mat[r][c]
        
        # part 2: get max side
        max_side = 0
        for r in range(ROWS):
            for c in range(COLS):
                if min(r, c) >= max_side:
                    curr = prefix[r+1][c+1]
                    top = prefix[r - max_side][c+1]
                    left = prefix[r+1][c - max_side]
                    topleft = prefix[r-max_side][c-max_side]
                    total = curr - top - left + topleft

                    if total <= threshold:
                        max_side += 1
        return max_side

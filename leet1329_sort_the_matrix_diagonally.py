class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        diago = defaultdict(list)
        for r in range(rows):
            for c in range(cols):
                diago[r - c].append(mat[r][c])
        # decremental sort
        for line in diago:
            diago[line].sort(reverse=True)
        
        # pop back --> incremental order
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = diago[r - c].pop()
        return mat

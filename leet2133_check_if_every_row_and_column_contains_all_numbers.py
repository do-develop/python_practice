class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)

        for i in range(N):
            if len(set(matrix[i])) != N:
                return False
            
            vertical = set()
            for j in range(N):
                vertical.add(matrix[j][i])
            if len(vertical) != N:
                return False
        return True
            

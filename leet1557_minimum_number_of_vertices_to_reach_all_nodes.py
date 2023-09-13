class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        hasIndegree = set(j for i, j in edges)
        for i in range(n):
            if i not in hasIndegree:
                res.append(i)
        return res

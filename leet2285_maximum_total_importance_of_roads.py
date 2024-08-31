class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n

        for edge in roads:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        
        degree.sort()
        value = 1
        total = 0
        for d in degree:
            total += value * d
            value += 1
        
        return total

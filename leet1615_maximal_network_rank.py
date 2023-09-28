class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        max_rank = 0
        for x in range(n):
            for y in range(x + 1, n):
                rank = len(graph[x]) + len(graph[y])
                if x in graph[y] or y in graph[x]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank

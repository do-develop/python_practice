class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range (n)]
        seen = [False] * n
        heap = [[0, 0]]

        for x, y, s, e in edges:
            graph[x].append([y, s, e])
        
        while heap:
            time, node = heappop(heap)
            if node == n - 1:
                return time
            if seen[node]:
                continue
            seen[node] = True
            for y, s, e in graph[node]:
                if time <= e and not seen[y]:
                    heappush(heap, [max(s, time) + 1, y])
        return -1

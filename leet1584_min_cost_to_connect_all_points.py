class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST - minimum spanning tree
        # Prim's algorithm approach
        # - visit (hashset) to avoid cycle, loop ends when the length == n - 1
        # - frontier (min-heap)
        N = len(points)
        adj = {i: [] for i in range(N)} # i : list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1- y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's algorithm 
        total = 0
        visit = set()
        min_heap =[[0, 0]] # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                continue
            total += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(min_heap, [nei_cost, nei])
        return total


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        heap, ans = [(0, 0)], [-1] * n

        for x, y, dist in edges:
            graph[x].append((dist, y))
            graph[y].append((dist, x))

        while heap:
            dist1, node = heappop(heap)
            if ans[node] != -1: continue

            ans[node] = dist1

            for dist2, neigh in graph[node]:
                dist2 += dist1
                if dist2 >= disappear[neigh]: continue
                heappush(heap, (dist2, neigh))

        return ans

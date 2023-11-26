class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # construct graph
        if n == 1: return 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        # dijkstra to get shortest path
        def dijkstra():
            min_heap = [(0, n)] # distance, node
            dist = [float('inf')] * (n + 1)
            dist[n] = 0
            while min_heap:
                d, src = heappop(min_heap)
                if d != dist[src]: # if d > dist[src], ignore
                    continue
                for w, nei in graph[src]:
                    if dist[nei] > dist[src] + w:
                        dist[nei] = dist[src] + w
                        heappush(min_heap, (dist[nei], nei))
            return dist
        
        @lru_cache(None)
        def dfs(src):
            if src == n: # found a path to reach the destination
                return 1
            ans = 0
            for _, nei in graph[src]:
                if dist[src] > dist[nei]:
                    ans = (ans + dfs(nei)) % 1000_000_007
            return ans
        
        dist = dijkstra()
        return dfs(1)

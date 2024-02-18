class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Dijkstra algorithm
        graph = defaultdict(list)
        for src, dst, time in roads:
            graph[src].append([dst, time])
            graph[dst].append([src, time])
        
        def dijkstra(src):
            distance = [math.inf] * n
            ways = [0] * n
            min_heap = [(0, src)] # (distance, source) starts from the 0 node
            # distance and ways to self
            distance[src] = 0
            ways[src] = 1

            while min_heap:
                dist, src = heappop(min_heap)
                if distance[src] < dist:
                    continue # dist is not updated yet
                for dst, time in graph[src]:
                    if distance[dst] > dist + time:
                        distance[dst] = dist + time
                        ways[dst] = ways[src]
                        heappush(min_heap, (distance[dst], dst))
                    elif distance[dst] == dist + time:
                        ways[dst] = (ways[dst] + ways[src]) % 1_000_000_007
            return ways[n - 1]

        return dijkstra(0)

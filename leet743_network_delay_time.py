class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for source, target, time in times:
            edges[source].append((target, time))
        
        visited = set()
        minHeap = [(0, k)] # (cost, node)
        total_time = 0

        while minHeap:
            cost, cur = heapq.heappop(minHeap)
            if cur in visited:
                continue
            visited.add(cur)
            total_time  = max(total_time, cost)

            for nei, neiCost in edges[cur]:
                if nei not in visited:
                    heapq.heappush(minHeap,(neiCost + cost, nei))
            
        return total_time if len(visited) == n else -1

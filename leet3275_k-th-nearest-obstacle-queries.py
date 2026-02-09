class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        # using max-heap of size k
        N = len(queries)
        distances = []
        res = []

        for i in range(N):
            dist = abs(queries[i][0]) + abs(queries[i][1])
            heapq.heappush(distances, -dist)
            if len(distances) > k:
                heapq.heappop(distances)
            res.append(-distances[0] if len(distances) == k else -1)
        return res

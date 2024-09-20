class Solution:
    def fillCups(self, amount: List[int]) -> int:
        times = 0
        max_heap = []

        for amt in amount:
            if amt != 0:
                heapq.heappush(max_heap, -amt)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            first += 1
            second += 1
            times += 1

            if first:
                heapq.heappush(max_heap, first)
            if second:
                heapq.heappush(max_heap, second)
        
        if max_heap:
            return times - max_heap[0]
        else:
            return times

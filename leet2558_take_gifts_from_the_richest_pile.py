class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-val for val in gifts]
        heapq.heapify(maxHeap)

        while k > 0:
            val = -heapq.heappop(maxHeap)
            next_val = int(math.floor(math.sqrt(val)))
            heapq.heappush(maxHeap, -next_val)
            k -= 1
        return -sum(maxHeap)

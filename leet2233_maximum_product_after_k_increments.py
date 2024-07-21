class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        
        for _ in range(k):
            mini = heapq.heappop(heap)
            heapq.heappush(heap, mini + 1)
        
        res = 1
        while len(heap) > 0:
            x = heapq.heappop(heap)
            res = res * x % (10**9+7)
        
        return res

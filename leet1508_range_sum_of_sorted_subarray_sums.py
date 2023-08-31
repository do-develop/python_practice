class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = [(x, i) for i, x in enumerate(nums)] # min-heap
        heapify(heap)

        total = 0
        for k in range(1, right+1): # 1-indexed
            x, i = heappop(heap)
            if k >= left: 
                total += x
            if i + 1 < len(nums):
                heappush(heap, (x + nums[i+1], i+1))
        return total % 1_000_000_007

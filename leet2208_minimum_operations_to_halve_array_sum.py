class Solution:
    def halveArray(self, nums: List[int]) -> int:
        # Need to havle the largest element
        # Heap or priority queue to query the maximum element
        q = []
        total = 0

        for n in nums:
            total += n
            heappush(q, -n)

        half = total / 2
        ops = 0 # count of operations
        while total > half:
            largest = heappop(q)
            halved_n = -(largest / 2)
            heappush(q, -halved_n)
            ops += 1
            total -= halved_n

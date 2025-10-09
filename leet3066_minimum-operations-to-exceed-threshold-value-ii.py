class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0

        curr = heappop(nums)
        while curr < k:
            nxt = 2 * curr + heappop(nums)
            curr = heappushpop(nums, nxt)
            ops += 1
        
        return ops

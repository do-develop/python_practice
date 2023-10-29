class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        highestK = [(-nums[0], 0)]
        max_sofar = nums[0]

        for i in range(1, len(nums)):
            while highestK[0][1] < i - k:
                heapq.heappop(highestK)
            max_sofar = nums[i] + -highestK[0][0]
            heapq.heappush(highestK, (-max_sofar, i))
        return max_sofar
